import pytest


query = """
    mutation SellDirect($input: SellDirectInput!) {
        sellDirect(input: $input) {
            event {
                eventType
                inventoryChanges {
                    product {
                        id
                        name
                        count
                    }
                    value
                }
            }
        }
    }
"""


@pytest.fixture
def products(product_factory):
    return (
        product_factory(name="product_1", count=100),
        product_factory(name="product_2", count=100),
    )


@pytest.fixture
def inventory_changes(products):
    product_1, product_2 = products
    return [
        {"productId": product_1.id, "value": product_1.count},
        {"productId": product_2.id, "value": product_2.count},
    ]


@pytest.fixture
def invalid_inventory_changes(products):
    product_1, product_2 = products
    return [
        {"productId": product_1.id, "value": product_1.count + 1},
        {"productId": product_2.id, "value": product_2.count},
    ]


@pytest.fixture
def empty_inventory_changes():
    return []


@pytest.mark.parametrize(
    "changes, expected_result",
    [
        ("inventory_changes", True),
        ("invalid_inventory_changes", False),
        ("empty_inventory_changes", False),
    ],
)
def test_sell_direct(snapshot, client, request, changes, expected_result):
    response = client.execute(
        query,
        variable_values={
            "input": {"inventoryChanges": request.getfixturevalue(changes)}
        },
    )
    snapshot.assert_match(response)
    assert bool(response["data"]["sellDirect"]) == expected_result
