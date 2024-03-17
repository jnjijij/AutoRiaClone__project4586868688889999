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
    Filters=[{'Name': 'tag:Name', 'Values': ['your-instance-name']}]
)

instance = instances[0]
instance.wait_until_running()
instance.reload()
instance.stop()
instance.wait_until_stopped()
instance.start()
instance.wait_until_running()

print(instance.public_dns_name)

def launch_instance():
    instances = ec2.create_instances(
        ImageId='ami-0c94855ba95c574c8',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='my-key-pair',
        SecurityGroupIds=['my-security-group'],
    )
    return instances[0]