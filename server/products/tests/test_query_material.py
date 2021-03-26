from graphql.language.ast import Variable


def test_query(client, product_material_factory):
    material = product_material_factory()
    query = """
        query ($id: Int!) {
            material(id: $id) {
                id
                name
            }
        }
    """
    response = client.execute(query, variable_values={"id": material.id})
    assert response["data"]["material"]["name"] == material.name
