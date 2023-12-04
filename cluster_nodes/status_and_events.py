"""
https://docs.couchbase.com/server/current/rest-api/rest-rebalance-overview.html
"""
from cb_server_rest_util.connection import CBRestConnection


class StatusAndEventsAPI(CBRestConnection):
    def __init__(self):
        super(StatusAndEventsAPI, self).__init__()

    def cluster_tasks(self):
        """
        GET /pools/default/tasks
        docs.couchbase.com/server/current/rest-api/rest-get-cluster-tasks.html
        """

    def rebalance_report(self, report_id):
        """
        GET /logs/rebalanceReport?reportID=<report-id>
        docs.couchbase.com/server/current/rest-api/rest-get-cluster-tasks.html
        """

    def cluster_info(self):
        """
        GET /pools
        docs.couchbase.com/server/current/rest-api/rest-cluster-get.html
        """
        api = self.base_url + "/pools"
        status, response = self.request(api, CBRestConnection.GET)
        content = response.json() if status else response.text
        return status, content

    def cluster_details(self):
        """
        GET /pools/default
        docs.couchbase.com/server/current/rest-api/rest-cluster-details.html
        """
        api = self.base_url + "/pools/default"
        status, response = self.request(api, CBRestConnection.GET)
        content = response.json() if status else response.text
        return status, content
