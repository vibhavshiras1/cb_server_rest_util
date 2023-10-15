"""
https://docs.couchbase.com/server/current/rest-api/rest-rebalance-overview.html
"""
from cb_server_rest_util.connection import CBRestConnection


class SettingsAndConnectionsAPI(CBRestConnection):
    def __init__(self):
        super(SettingsAndConnectionsAPI, self).__init__()
