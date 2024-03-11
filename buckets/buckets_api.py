from cb_server_rest_util.buckets.bucket_info import BucketInfo
from cb_server_rest_util.buckets.bucket_stats import BucketStats
from cb_server_rest_util.buckets.manage_bucket import BucketManageAPI


class BucketRestApi(BucketManageAPI, BucketInfo, BucketStats):
    def __init__(self, server):
        super(BucketRestApi, self).__init__()

        self.set_server_values(server)
        self.set_endpoint_urls(server)
