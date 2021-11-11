import unittest

from s3_api import *


class S3ApiTest(unittest.TestCase):

    def test_download(self):
        bucket = 'beppe-udacity'
        key = 'capstone/us-cities-demographics.csv'
        filename = '../tmp/us-cities-demographics.csv'

        download_object(bucket, key, filename)

    def test_upload(self):
        bucket = 'beppe-udacity'
        key = 'doc/S3.md'
        filename = '../../doc/S3.md'

        upload_object(bucket, key, filename)

    def test_bucket_list(self):

        buckets = bucket_list()
        print(buckets)

