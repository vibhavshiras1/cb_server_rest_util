from cb_server_rest_util.connection import CBRestConnection


class Certicates(CBRestConnection):
    def __init__(self):
        super(Certicates, self).__init__()

    def get_trusted_root_certificates(self):
        """
        GET:: /pools/default/trustedCAs
        docs.couchbase.com/server/current/rest-api/rbac.html
        """
        url = "/pools/default/trustedCAs"
        api = self.base_url + url
        status, content, _ = self.request(api, self.GET)
        return status, content

    def get_node_certificates(self):
        url = "/pools/default/certificates"
        api = self.base_url + url
        status, content, _ = self.request(api, self.GET)
        return status, content