def test_list_query(snapshot, client, product_category_factory):
    for n in range(3):
        product_category_factory(name=f"category_{n}")
    query = """
        query AllCategories {
            allCategories {
                id
                name
            }
        }
    """
    response = client.execute(query)
    snapshot.assert_match(response)


def test_retrieve_query(snapshot, client, product_category_factory):
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


def test_retrieve_query_with_related_object(
    snapshot, client, product_factory, product_category_factory,
):
    category = product_category_factory(name="category")
    for n in range(3):
        product_factory(name=f"product_{n}", categories=[category])

    query = """
        query ($id: Int!) {
            category(id: $id) {
                id
                name
                products {
                    id
                    name
                }
            }
        }
    """
    response = client.execute(query, variable_values={"id": category.id})
    snapshot.assert_match(response)
