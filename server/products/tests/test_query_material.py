def test_list_query(snapshot, client, product_material_factory):
    for n in range(3):
        product_material_factory(name=f"material_{n}")
    query = """
        query AllMaterials {
            allMaterials {
                id
                name
            }
        }
    """
    response = client.execute(query)
    snapshot.assert_match(response)


def test_retrieve_query(snapshot, client, product_material_factory):
    material = product_material_factory(name="material")
    query = """
        query ($id: Int!) {
            material(id: $id) {
                id
                name
            }
        }
    """
    response = client.execute(query, variable_values={"id": material.id})
    snapshot.assert_match(response)


def test_retrieve_query_with_related_object(
    snapshot,
    client,
    product_factory,
    product_material_factory,
):
    material = product_material_factory(name="material")
    for n in range(3):
        product_factory(name=f"product_{n}", materials=[material])

    query = """
        query ($id: Int!) {
            material(id: $id) {
                id
                name
                products {
                    id
                    name
                }
            }
        }
    """
    response = client.execute(query, variable_values={"id": material.id})
    snapshot.assert_match(response)
