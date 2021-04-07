import pytest

query = """
    mutation OrderProduct($input: OrderProductInput!) {
        orderProduct(input: $input) {
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
        product_factory(name="product_1", count=0),
        product_factory(name="product_2", count=0),
    )


@pytest.fixture
def inventory_changes(products):
    product_1, product_2 = products
    return [
        {"productId": product_1.id, "value": 100},
        {"productId": product_2.id, "value": 100},
    ]


@pytest.fixture
def zero_inventory_changes(products):
    product_1, product_2 = products
    return [
        {"productId": product_1.id, "value": 0},
        {"productId": product_2.id, "value": 0},
    ]
@pytest.fixture
def minus_inventory_changes(products):
    product_1, product_2 = products
    return [
        {"productId": product_1.id, "value": -1},
        {"productId": product_2.id, "value": -1},
    ]


@pytest.fixture
def empty_inventory_changes():
    return []


@pytest.mark.parametrize(
    "changes, expected_result",
    [
        ("inventory_changes", True),
        ("zero_inventory_changes", False),
        ("minus_inventory_changes", False),
        ("empty_inventory_changes", False),
    ],
)
def test_order_product(snapshot, client, request, changes, expected_result):
    response = client.execute(
        query,
        variable_values={
            "input": {"inventoryChanges": request.getfixturevalue(changes)}
        },
    )
    snapshot.assert_match(response)
    assert bool(response["data"]["orderProduct"]) == expected_result
