"""
https://docs.couchbase.com/server/current/rest-api/rest-index-service.html
"""

from cb_server_rest_util.connection import CBRestConnection


class IndexSettings(CBRestConnection):
    def __init__(self):
        super(IndexSettings).__init__()

    def get_gsi_settings(self):
        """
        GET :: /settings/indexes
        docs.couchbase.com/server/current/rest-api/get-settings-indexes.html
        """

    def set_gsi_settings(self, gsi_settings_dict):
        """
        POST :: /settings/indexes
        """
        api = self.base_url + '/settings/indexes'
        status, content, _ = self.request(api, 'POST', gsi_settings_dict)
        return status, content

    def get_node_statistics(self):
        """
        GET :: /api/v1/stats
        """

    def get_keyspace_statistics(self, key_space):
        """
        GET :: /api/v1/stats/{keyspace}
        """

    def get_index_statistics(self, key_space, index_name):
        """
        GET :: /api/v1/stats/{keyspace}/{index}
        """
