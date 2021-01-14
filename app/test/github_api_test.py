import unittest

from github_api import check_file_exist, get_file, put_file


class GithubApiTest(unittest.TestCase):

    def test_check_file_exist(self):
        seq = check_file_exist("/files/file.json")

        self.assertTrue(seq)

    def test_check_file_does_not_exist(self):
        seq = check_file_exist("files/notfound.json")

        self.assertFalse(seq)

    def test_get_file(self):
        seq = get_file("files/file.json")

        self.assertIsNotNone(seq)

    def test_put_file(self):
        seq = put_file("files/file.json", "{name: \"Beppe\", city: \"Amsterdam\"};")


