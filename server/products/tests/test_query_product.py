def test_list_query(snapshot, client, product_factory):
    for n in range(3):
        product_factory(name=f"product_{n}")
    query = """
        query AllProducts {
            allProducts {
                id
                name
            }
        }
    """
    response = client.execute(query)
    snapshot.assert_match(response)


def test_retrieve_query(snapshot, client, product_factory):
    product = product_factory(name="product")
    query = """
        query ($id: Int!) {
            product(id: $id) {
                id
                name
            }
        }
    """
    response = client.execute(query, variable_values={"id": product.id})
    snapshot.assert_match(response)
