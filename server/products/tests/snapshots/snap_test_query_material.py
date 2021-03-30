# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_list_query 1'] = {
    'data': {
        'allMaterials': [
            {
                'id': '1',
                'name': 'material_0'
            },
            {
                'id': '2',
                'name': 'material_1'
            },
            {
                'id': '3',
                'name': 'material_2'
            }
        ]
    }
}

snapshots['test_retrieve_query 1'] = {
    'data': {
        'material': {
            'id': '1',
            'name': 'material'
        }
    }
}

snapshots['test_retrieve_query_with_related_object 1'] = {
    'data': {
        'material': {
            'id': '1',
            'name': 'material',
            'products': [
                {
                    'id': '1',
                    'name': 'product_0'
                },
                {
                    'id': '2',
                    'name': 'product_1'
                },
                {
                    'id': '3',
                    'name': 'product_2'
                }
            ]
        }
    }
}
