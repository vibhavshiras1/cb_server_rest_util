"""
https://docs.couchbase.com/server/current/rest-api/rest-index-service.html
"""

from rest_api.connection import CBRestConnection


class QuerySettings(CBRestConnection):
    def __init__(self):
        super(QuerySettings).__init__()
