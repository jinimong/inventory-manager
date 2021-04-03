# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_mutation 1'] = {
    'data': {
        'createCategory': {
            'category': {
                'id': '1',
                'name': 'category'
            }
        }
    }
}

snapshots['test_create_mutation_fail_by_duplication 1'] = {
    'data': {
        'createCategory': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 9,
                    'line': 3
                }
            ],
            'message': 'UNIQUE constraint failed: products_productcategory.name',
            'path': [
                'createCategory'
            ]
        }
    ]
}
