query = """
    mutation CreateProductCategory($name: String!) {
        createCategory(name: $name) {
            category {
                id
                name
            }
        }
    }
"""


def test_create_mutation(snapshot, client):
    response = client.execute(query, variable_values={"name": "category"})
    snapshot.assert_match(response)


def test_create_mutation_fail_by_duplication(
    snapshot, product_category_factory, client
):
    duplicated_name = "category"
    product_category_factory(name=duplicated_name)
    response = client.execute(query, variable_values={"name": duplicated_name})
    snapshot.assert_match(response)
