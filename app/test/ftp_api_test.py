import unittest

from ftp_api import *


class FtpApiTest(unittest.TestCase):

    def test_download(self):
        filename = '/files/us-cities-demographics.csv'
        tmpfile = 'tmp/us-tmp.csv'

        content = download_file(filename, tmpfile)

        print(content)

    def test_upload(self):
        filename = '/files/us-cities-demographics.csv'
        localfile= 'tmp/us-cities-demographics.csv'

        upload_file(filename, localfile)
