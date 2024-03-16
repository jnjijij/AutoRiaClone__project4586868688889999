import boto3

s3 = boto3.resource("s3")

# Create a bucket
bucket = s3.Bucket("my-new-bucket")
bucket.create()

# Upload a file
data = open("my-file.txt", "rb")
s3.Bucket("my-new-bucket").put_object(Key="my-file.txt", Body=data)