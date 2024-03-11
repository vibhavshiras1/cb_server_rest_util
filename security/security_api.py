from cb_server_rest_util.security.auditing import Auditing
from cb_server_rest_util.security.rbac_authorization import RbacAuthorization
from cb_server_rest_util.security.restrict_node_addition import \
    NodeInitAddition


class SecurityRestAPI(Auditing, NodeInitAddition, RbacAuthorization):
    def __init__(self, server):
        super(SecurityRestAPI, self).__init__()

        self.set_server_values(server)
        self.set_endpoint_urls(server)
