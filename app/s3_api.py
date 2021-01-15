import boto3
import os

from config import get_aws_access_key_id, get_aws_secret_access_key

session = boto3.session.Session()


s3 = session.client(
    service_name='s3',
    aws_access_key_id=get_aws_access_key_id(),
    aws_secret_access_key=get_aws_secret_access_key()
)


def download_object(bucket_name, key, filename):
    print(f"filename {filename}")

    print(filename)

    s3.download_file(Bucket=bucket_name, Key=key, Filename=filename)

    print(f"Object {key} has been downloaded to " + filename)

    return filename


def upload_object(bucket_name, key, filename):
    print(f"filename {filename}")

    s3.upload_file(Bucket=bucket_name, Key=key, Filename=filename)

    print(f"File {filename} has been uploaded to {bucket_name}:{key}")

    return key