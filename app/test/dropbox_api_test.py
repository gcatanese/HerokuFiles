import unittest

from dropbox_api import *


class DropboxApiTest(unittest.TestCase):

    def test_download(self):
        filename = '/files/us-cities-demographics.csv'

        download_file(filename)

    def test_upload(self):
        filename = '/files/us-cities-demographics.csv'
        localfile= 'tmp/us-cities-demographics.csv'

        upload_file(filename, localfile)
