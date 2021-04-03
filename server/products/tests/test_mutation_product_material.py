query = """
    mutation CreateProductMaterial($name: String!) {
        createMaterial(name: $name) {
            material {
                id
                name
            }
        }
    }
"""


def test_create_mutation(snapshot, client):
    response = client.execute(query, variable_values={"name": "material"})
    snapshot.assert_match(response)


def test_create_mutation_fail_by_duplication(
    snapshot, product_material_factory, client
):
    duplicated_name = "material"
    product_material_factory(name=duplicated_name)
    response = client.execute(query, variable_values={"name": duplicated_name})
    snapshot.assert_match(response)
