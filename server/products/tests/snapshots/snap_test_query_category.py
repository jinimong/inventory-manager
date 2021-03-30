# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_list_query 1'] = {
    'data': {
        'allCategories': [
            {
                'id': '1',
                'name': 'category_0'
            },
            {
                'id': '2',
                'name': 'category_1'
            },
            {
                'id': '3',
                'name': 'category_2'
            }
        ]
    }
}

snapshots['test_retrieve_query 1'] = {
    'data': {
        'category': {
            'id': '1',
            'name': 'category'
        }
    }
}

snapshots['test_retrieve_query_with_related_object 1'] = {
    'data': {
        'category': {
            'id': '1',
            'name': 'category',
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
