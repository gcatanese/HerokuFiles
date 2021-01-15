import unittest

from google_api import *

class GoogleApiTest(unittest.TestCase):

    def test_create_file(self):
        create_file("")
        self.assertTrue(True)

