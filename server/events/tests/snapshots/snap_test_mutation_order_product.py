# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_order_product[empty_inventory_changes-False] 1'] = {
    'data': {
        'orderProduct': {
            'event': {
                'eventType': 'OP',
                'inventoryChanges': [
                ]
            }
        }
    }
}

snapshots['test_order_product[inventory_changes-True] 1'] = {
    'data': {
        'orderProduct': {
            'event': {
                'eventType': 'OP',
                'inventoryChanges': [
                    {
                        'product': {
                            'count': 100,
                            'id': '1',
                            'name': 'product_1'
                        },
                        'value': 100
                    },
                    {
                        'product': {
                            'count': 100,
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

snapshots['test_order_product[minus_inventory_changes-False] 1'] = {
    'data': {
        'orderProduct': None
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
                'orderProduct'
            ]
        }
    ]
}

snapshots['test_order_product[zero_inventory_changes-False] 1'] = {
    'data': {
        'orderProduct': {
            'event': {
                'eventType': 'OP',
                'inventoryChanges': [
                    {
                        'product': {
                            'count': 0,
                            'id': '1',
                            'name': 'product_1'
                        },
                        'value': 0
                    },
                    {
                        'product': {
                            'count': 0,
                            'id': '2',
                            'name': 'product_2'
                        },
                        'value': 0
                    }
                ]
            }
        }
    }
}
