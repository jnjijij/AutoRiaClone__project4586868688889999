import boto3

sns = boto3.client("sns")

topic_name = "my-topic"
response = sns.create_topic(Name=topic_name)
topic_arn = response["TopicArn"]

# Publish a message
message = "Hello, SNS!"
response = sns.publish(TopicArn=topic_arn, Message=message)

print(f"Message published: {response['MessageId']}")