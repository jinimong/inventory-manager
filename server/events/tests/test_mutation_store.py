query = """
    mutation CreateStore($name: String!) {
        createStore(name: $name) {
            store {
                id
                name
            }
        }
    }
"""


def test_create_store(snapshot, client):
    response = client.execute(query, variable_values={"name": "store"})
    snapshot.assert_match(response)


def test_create_mutation_fail_by_duplication(snapshot, store_factory, client):
    duplicated_name = "store"
    store_factory(name=duplicated_name)
    response = client.execute(query, variable_values={"name": duplicated_name})
    snapshot.assert_match(response)
