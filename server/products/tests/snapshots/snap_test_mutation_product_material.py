# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_mutation 1'] = {
    'data': {
        'createMaterial': {
            'material': {
                'id': '1',
                'name': 'material'
            }
        }
    }
}

snapshots['test_create_mutation_fail_by_duplication 1'] = {
    'data': {
        'createMaterial': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 9,
                    'line': 3
                }
            ],
            'message': 'UNIQUE constraint failed: products_productmaterial.name',
            'path': [
                'createMaterial'
            ]
        }
    ]
}
