import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_github_access_token():
    return os.environ.get("GITHUB_ACCESS_TOKEN", "")