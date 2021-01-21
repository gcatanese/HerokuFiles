import unittest

from gitlab_api import *


class GitlabApiTest(unittest.TestCase):

    def test_check_file_exist(self):
        seq = check_file_exist("files/config.json")

        self.assertTrue(seq)

    def test_check_file_does_not_exist(self):
        seq = check_file_exist("files/notfound.json")

        self.assertFalse(seq)

    def test_get_file(self):
        seq = get_file("files/config.json")

        self.assertIsNotNone(seq)

    def test_put_file(self):
        seq = put_file("files/file.json", "{name: \"Beppe\", city: \"Amsterdam\"};")
