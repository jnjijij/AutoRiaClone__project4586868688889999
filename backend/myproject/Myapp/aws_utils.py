import boto3


def get_s3_client():
    """
    Function to create and return an S3 client using boto3
    """
    AWS_ACCESS_KEY_ID = 'your_access_key_id'
    AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'

    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    return session.client('s3')


def upload_file_to_s3(file_path, bucket_name, object_name):
    """
    Function to upload a file to an S3 bucket
    """
    s3_client = get_s3_client()
    s3_client.upload_file(file_path, bucket_name, object_name)

