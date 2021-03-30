# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_query 1'] = {
    'data': {
        'category': {
            'id': '1',
            'name': 'category'
        }
    }
}
