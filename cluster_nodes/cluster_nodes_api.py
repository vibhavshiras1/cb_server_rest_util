from rest_api.cluster_nodes.cluster_init_provision \
    import ClusterInitializationProvision
from rest_api.cluster_nodes.rebalance import RebalanceRestAPI


class ClusterRestAPI(ClusterInitializationProvision, RebalanceRestAPI):
    def __init__(self, server):
        """
        Main gateway for all Cluster Rest Operations
        """
        super(ClusterRestAPI, self).__init__()

        self.set_server_values(server)
        self.set_endpoint_urls(server)
        self.check_if_couchbase_is_active(self, max_retry=5)
