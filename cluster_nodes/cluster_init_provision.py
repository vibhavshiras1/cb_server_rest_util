"""
https://docs.couchbase.com/server/current/rest-api/rest-cluster-init-and-provisioning.html
https://docs.couchbase.com/server/current/rest-api/rest-adding-and-removing-nodes.html
"""
from rest_api.connection import CBRestConnection


class ClusterInitializationProvision(CBRestConnection):
    def __init__(self):
        super(ClusterInitializationProvision).__init__()

    def initialize_cluster(self, hostname, username, password,
                           data_path=None, index_path=None,
                           cbas_path=None, eventing_path=None,
                           java_home=None, send_stats=None,
                           cluster_name=None, services="kv",
                           memory_quota=None, index_memory_quota=None,
                           eventing_memory_quota=None, fts_memory_quota=None,
                           cbas_memory_quota=None,
                           afamily=None, afamily_only=None,
                           node_encryption=None, indexer_storage_mode=None,
                           port='SAME', allowed_hosts=None):
        """
        POST /clusterInit
        docs.couchbase.com/server/current/rest-api/rest-initialize-cluster.html
        """
        raise NotImplementedError()

    def initialize_node(self):
        """
        POST /nodes/self/controller/settings
        docs.couchbase.com/server/current/rest-api/rest-initialize-node.html
        """
        raise NotImplementedError()

    def establish_credentials(self, username, password, port="SAME"):
        """
        POST /settings/web
        docs.couchbase.com/server/current/rest-api/rest-establish-credentials.html
        """
        raise NotImplementedError()

    def rename_node(self, hostname):
        """
        POST /node/controller/rename
        docs.couchbase.com/server/current/rest-api/rest-name-node.html
        """
        raise NotImplementedError()

    def configure_memory(self):
        """
        POST /pools/default
        docs.couchbase.com/server/current/rest-api/rest-configure-memory.html
        """
        raise NotImplementedError()

    def setup_services(self):
        """
        POST /node/controller/setupServices
        docs.couchbase.com/server/current/rest-api/rest-set-up-services.html
        """
        raise NotImplementedError()

    def naming_the_cluster(self):
        """
        POST /node/controller/setupServices
        docs.couchbase.com/server/current/rest-api/rest-name-cluster.html
        """
        raise NotImplementedError()
