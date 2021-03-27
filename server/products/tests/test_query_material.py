def test_query(snapshot, client, product_material_factory):
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
