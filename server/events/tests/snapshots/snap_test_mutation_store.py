# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_mutation_fail_by_duplication 1'] = {
    'data': {
        'createStore': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 9,
                    'line': 3
                }
            ],
            'message': 'UNIQUE constraint failed: events_store.name',
            'path': [
                'createStore'
            ]
        }
    ]
}

snapshots['test_create_store 1'] = {
    'data': {
        'createStore': {
            'store': {
                'id': '1',
                'name': 'store'
            }
        }
    }
}
