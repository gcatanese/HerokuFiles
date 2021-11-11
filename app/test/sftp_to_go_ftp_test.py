import unittest

from sftp_to_go_ftp import *


class SftpToGoFtpTest(unittest.TestCase):

    def test_download(self):
        filename = 'doc/S3.md'
        tmpfile = '../tmp/S3.md'
        content = download_file(filename, tmpfile)

        print(content)

    def test_upload(self):
        filename = 'doc/Github.md'
        localfile = '../../doc/Github.md'

        upload_file(filename, localfile)
