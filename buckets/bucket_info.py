from requests.utils import quote
from cb_server_rest_util.connection import CBRestConnection


class BucketInfo(CBRestConnection):
    def __init__(self):
        super(BucketInfo, self).__init__()

    def get_bucket_info(self, bucket_name=None):
        """
        GET :: /pools/default/buckets
        docs.couchbase.com/server/current/rest-api/rest-buckets-summary.html
        """
        api = self.base_url + "/pools/default/buckets"
        if bucket_name:
            bucket_name = quote(bucket_name)
            api += f"/{bucket_name}"
        status, content, _ = self.request(api)
        return status, content
