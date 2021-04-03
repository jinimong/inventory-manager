from django.core.files.uploadedfile import SimpleUploadedFile


def test_create_mutation(snapshot, file_upload_client, use_test_media_root):
    query = """
        mutation CreateProduct($productInput: ProductInput) {
            createProduct(productInput: $productInput) {
                product {
                    id
                    name
                    images {
                        photo
                        photoThumbnail
                    }
                }
            }
        }
    """
    response = file_upload_client(
        query,
        op_name="CreateProduct",
        variables={
            "productInput": {
                "name": "product",
                "price": 2000,
                "priceWithPees": 2500,
                "images": [{"photo": None}, {"photo": None}],
            }
        },
        files={
            "productInput.images.0.photo": SimpleUploadedFile(
                "photo_1.jpg",
                b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b",
                content_type="image/jpeg",
            ),
            "productInput.images.1.photo": SimpleUploadedFile(
                "photo_2.jpg",
                b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b",
                content_type="image/jpeg",
            ),
        },
    )
    snapshot.assert_match(response.json())
