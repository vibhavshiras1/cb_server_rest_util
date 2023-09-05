"""
https://docs.couchbase.com/server/current/rest-api/rest-index-service.html
"""

from rest_api.connection import CBRestConnection


class AdminRest(CBRestConnection):
    def __init__(self):
        super(AdminRest).__init__()
