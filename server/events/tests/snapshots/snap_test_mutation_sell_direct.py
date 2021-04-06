# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_sell_direct 1'] = {
    'data': {
        'sellDirect': {
            'event': {
                'description': 'Sell Direct Description',
                'eventType': 'SD',
                'inventoryChanges': [
                    {
                        'product': {
                            'id': '1',
                            'name': 'product_1'
                        },
                        'value': 100
                    },
                    {
                        'product': {
                            'id': '2',
                            'name': 'product_2'
                        },
                        'value': 100
                    }
                ]
            }
        }
    }
}

snapshots['test_sell_direct_fail_by_count_over 1'] = {
    'data': {
        'sellDirect': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 9,
                    'line': 3
                }
            ],
            'message': 'CHECK constraint failed: products_product',
            'path': [
                'sellDirect'
            ]
        }
    ]
}

snapshots['test_sell_direct_fail_without_inventory_changes 1'] = {
    'data': {
        'sellDirect': {
            'event': {
                'description': 'Invalid Sell Direct Description',
                'eventType': 'SD',
                'inventoryChanges': [
                ]
            }
        }
    }
}
