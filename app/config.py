import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_github_access_token():
    return os.environ.get("GITHUB_ACCESS_TOKEN", "")


def get_aws_access_key_id():
    return os.environ.get('AWS_ACCESS_KEY_ID')


def get_aws_secret_access_key():
    return os.environ.get('AWS_SECRET_ACCESS_KEY')


def get_dropbox_access_token():
    return os.environ.get("DROPBOX_ACCESS_TOKEN", "")


def get_ftp_host():
    return os.environ.get("FTP_HOST", "")


def get_ftp_username():
    return os.environ.get("FTP_USERNAME", "")


def get_ftp_password():
    return os.environ.get("FTP_PASSWORD", "")


def get_gitlab_access_token():
    return os.environ.get("GITLAB_ACCESS_TOKEN", "")


def get_gmail_username():
    return os.environ.get("GMAIL_USERNAME", "")


def get_gmail_password():
    return os.environ.get("GMAIL_PASSWORD", "")


def get_sftptogo_aws_access_key_id():
    return os.environ.get('SFTPTOGO_AWS_ACCESS_KEY_ID')


def get_sftptogo_aws_secret_access_key():
    return os.environ.get('SFTPTOGO_AWS_SECRET_ACCESS_KEY')


def get_sftptogo_aws_region():
    return os.environ.get('SFTPTOGO_AWS_REGION')


def get_sftptogo_aws_bucket_name():
    return os.environ.get('SFTPTOGO_AWS_BUCKET_NAME')
