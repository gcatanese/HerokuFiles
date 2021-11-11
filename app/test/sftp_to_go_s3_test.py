import unittest

from sftp_to_go_s3 import *


class SftpToGoS3Test(unittest.TestCase):

    def test_download(self):
        bucket = get_sftptogo_aws_bucket_name()
        key = 'doc/S3.md'
        filename = '../tmp/S3.md'

        download_object(bucket, key, filename)

    def test_upload(self):
        bucket = get_sftptogo_aws_bucket_name()
        key = 'doc/S3.md'
        filename = '../../doc/S3.md'

        upload_object(bucket, key, filename)

