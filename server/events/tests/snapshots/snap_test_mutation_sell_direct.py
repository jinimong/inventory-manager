# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_sell_direct[empty_inventory_changes-False] 1'] = {
    'data': {
        'sellDirect': {
            'event': {
                'eventType': 'SD',
                'inventoryChanges': [
                ]
            }
        }
    }
}

snapshots['test_sell_direct[invalid_inventory_changes-False] 1'] = {
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

snapshots['test_sell_direct[inventory_changes-True] 1'] = {
    'data': {
        'sellDirect': {
            'event': {
                'eventType': 'SD',
                'inventoryChanges': [
                    {
                        'product': {
                            'count': 0,
                            'id': '1',
                            'name': 'product_1'
                        },
                        'value': 100
                    },
                    {
                        'product': {
                            'count': 0,
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
