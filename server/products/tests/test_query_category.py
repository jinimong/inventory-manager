def test_query(snapshot, client, product_category_factory):
    category = product_category_factory(name="category")
    query = """
        query ($id: Int!) {
            category(id: $id) {
                id
                name
            }
        }
    """
    response = client.execute(query, variable_values={"id": category.id})
    snapshot.assert_match(response)
