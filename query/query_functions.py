"""
https://docs.couchbase.com/server/current/rest-api/rest-index-service.html
"""

from rest_api.connection import CBRestConnection


class QueryFunctions(CBRestConnection):
    def __init__(self):
        super(QueryFunctions).__init__()
