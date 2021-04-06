import pytest


query = """
    mutation SellDirect($input: SellDirectInput!) {
        sellDirect(input: $input) {
            event {
                eventType
                description
                inventoryChanges {
                    product {
                        id
                        name
                    }
                    value
                }
            }
        }
    }
"""


@pytest.fixture
def inventoryChanges(product_factory):
    product_1 = product_factory(name="product_1", count=100)
    product_2 = product_factory(name="product_2", count=100)
    return [
        {"productId": product_1.id, "value": product_1.count},
        {"productId": product_2.id, "value": product_2.count},
    ]


@pytest.fixture
def invalidInventoryChanges(product_factory):
    product_1 = product_factory(name="product_1", count=100)
    product_2 = product_factory(name="product_2", count=100)
    return [
        {"productId": product_1.id, "value": product_1.count + 1},
        {"productId": product_2.id, "value": product_2.count},
    ]


def test_sell_direct(snapshot, client, inventoryChanges):
    response = client.execute(
        query,
        variable_values={
            "input": {
                "description": "Sell Direct Description",
                "inventoryChanges": inventoryChanges,
            }
        },
    )
    snapshot.assert_match(response)


def test_sell_direct_fail_by_count_over(
    snapshot, client, invalidInventoryChanges
):
    response = client.execute(
        query,
        variable_values={
            "input": {
                "description": "Invalid Sell Direct Description",
                "inventoryChanges": invalidInventoryChanges,
            }
        },
    )
    snapshot.assert_match(response)
    assert response["data"]["sellDirect"] == None


def test_sell_direct_fail_without_inventory_changes(snapshot, client):
    response = client.execute(
        query,
        variable_values={
            "input": {
                "description": "Invalid Sell Direct Description",
                "inventoryChanges": [],
            }
        },
    )
    snapshot.assert_match(response)
    assert response["data"]["sellDirect"] == None
