"""
https://docs.couchbase.com/server/current/rest-api/rest-rebalance-overview.html
"""
from cb_server_rest_util.connection import CBRestConnection


class AutoFailoverAPI(CBRestConnection):
    def __init__(self):
        super(AutoFailoverAPI, self).__init__()
