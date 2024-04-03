from cb_server_rest_util.connection import CBRestConnection


class ManageServerGroups(CBRestConnection):
    def __init__(self):
        super(ManageServerGroups, self).__init__()

    def get_server_groups_info(self):
        """
        docs.couchbase.com/server/current/rest-api/rest-servergroup-get.html
        GET :: /pools/default/serverGroups
        """
        api = self.base_url + "/pools/default/serverGroups"
        status, content, _ = self.request(api, self.GET)
        return status, content

    def create_server_group(self, server_group_name):
        """
        docs.couchbase.com/server/current/rest-api/rest-servergroup-post-create.html
        POST :: /pools/default/serverGroups
        """
        api = self.base_url + "/pools/default/serverGroups"
        params = {"name": server_group_name}
        status, content, _ = self.request(api, self.POST, params=params)
        return status, content

    def rename_server_group(self, uuid, new_server_group_name):
        """
        docs.couchbase.com/server/current/rest-api/rest-servergroup-put.html
        PUT :: /pools/default/serverGroups/<uuid>
        """
        api = self.base_url + f"/pools/default/serverGroups/{uuid}"
        params = {"name": new_server_group_name}
        status, content, _ = self.request(api, self.PUT, params=params)
        return status, content

    def delete_server_group(self, uuid):
        """
        docs.couchbase.com/server/current/rest-api/rest-servergroup-delete.html
        DELETE :: /pools/default/serverGroups/<uuid>
        """
        api = self.base_url + f"/pools/default/serverGroups/{uuid}"
        status, content, _ = self.request(api, self.DELETE)
        return status, content
