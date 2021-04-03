# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_mutation 1'] = {
    'data': {
        'createProduct': {
            'product': {
                'id': '1',
                'images': [
                    {
                        'photo': '/media/test/photo_1.jpg',
                        'photoThumbnail': '/media/test/CACHE/images/photo_1/1c92775827def316cb8d32c40de1bb70.jpg'
                    },
                    {
                        'photo': '/media/test/photo_2.jpg',
                        'photoThumbnail': '/media/test/CACHE/images/photo_2/2929c69a42230a9d8aee6e969c0e7669.jpg'
                    }
                ],
                'name': 'product'
            }
        }
    }
}
