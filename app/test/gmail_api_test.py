import unittest

from gmail_api import *


class MailApiTest(unittest.TestCase):

    def test_upload(self):
        dest = "beppe@example.com"
        localfile= 'tmp/attach.txt'

        upload_file(dest, localfile)
