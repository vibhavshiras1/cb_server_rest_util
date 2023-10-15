"""
https://docs.couchbase.com/server/current/rest-api/rest-rebalance-overview.html
"""
from cb_server_rest_util.connection import CBRestConnection


class ManualFailoverAPI(CBRestConnection):
    def __init__(self):
        super(ManualFailoverAPI, self).__init__()
