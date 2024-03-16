import boto3

ec2 = boto3.resource("ec2")

# Create a new instance
instances = ec2.create_instances(
    ImageId="ami-0c55b159cbfafe1f0",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="my-key-pair",
    SecurityGroupIds=["sg-xxxxxxxx"],
)

instance = instances[0]
instance.wait_until_running()
instance.reload()

print(instance.public_dns_name)