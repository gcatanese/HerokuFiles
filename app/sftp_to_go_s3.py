import boto3

from config import *

# Integration with SFTP To Go (S3)

session = boto3.session.Session()


s3 = session.client(
    service_name='s3',
    aws_access_key_id=get_sftptogo_aws_access_key_id(),
    aws_secret_access_key=get_sftptogo_aws_secret_access_key(),
    region_name=get_sftptogo_aws_region()
)


def download_object(bucket_name, key, filename):
    """
    Get file from S3
    :param bucket_name: name of S3 bucket
    :param key: key of the file (ie /a/b/mydoc.txt)
    :param filename: path where to save the file
    :return:
    """
    print(f"filename {filename}")

    s3.download_file(Bucket=bucket_name, Key=key, Filename=filename)

    print(f"Object {key} has been downloaded to " + filename)

    return filename


def upload_object(bucket_name, key, filename):
    """
    Put file onto S3
    :param bucket_name: name of S3 bucket
    :param key: key of the file (ie /a/b/mydoc.txt)
    :param filename: path of the file to upload
    :return:
    """
    print(f"filename {filename}")

    s3.upload_file(Bucket=bucket_name, Key=key, Filename=filename)

    print(f"File {filename} has been uploaded to {bucket_name}:{key}")

    return key


