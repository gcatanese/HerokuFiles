import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_github_access_token():
    return os.environ.get("GITHUB_ACCESS_TOKEN", "")


def get_aws_access_key_id():
    return os.environ.get('AWS_ACCESS_KEY_ID')


def get_aws_secret_access_key():
    return os.environ.get('AWS_SECRET_ACCESS_KEY')
