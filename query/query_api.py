from rest_api.query.admin_rest import AdminRest
from rest_api.query.query_functions import QueryFunctions
from rest_api.query.query_settings import QuerySettings


class QueryRestAPI(AdminRest, QuerySettings, QueryFunctions):
    def __init__(self, server):
        super(QueryRestAPI).__init__()

        self.set_server_values(server)
        self.set_endpoint_urls(server)
        self.check_if_couchbase_is_active(self, max_retry=5)
