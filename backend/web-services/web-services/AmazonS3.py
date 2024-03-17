import boto3

s3 = boto3.resource("s3")

# Create a bucket
bucket = s3.Bucket("my-new-bucket")
bucket.create()

# Upload a file
data = open("my-file.txt", "rb")
s3.Bucket("my-new-bucket").put_object(Key="my-file.txt", Body=data)
s3 = boto3.client('s3')
s3.upload_file('path/to/local/file', 'your-bucket-name', 'path/to/s3/file')
def upload_file(file_name, bucket):
    s3.upload_file(file_name, bucket, file_name)