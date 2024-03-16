import boto3

sqs = boto3.client("sqs")

queue_name = "my-queue"
response = sqs.create_queue(QueueName=queue_name)
queue_url = response["QueueUrl"]

# Send a message
message_body = "Hello, SQS!"
response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)

# Receive a message
response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
message = response.get("Messages")
if message:
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message[0]["ReceiptHandle"])