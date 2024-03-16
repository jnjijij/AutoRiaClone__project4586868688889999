import boto3

rds = boto3.client("rds")

response = rds.create_db_instance(
    DBInstanceIdentifier="my-db-instance",
    AllocatedStorage=20,
    DBInstanceClass="db.t2.micro",
    Engine="postgres",
    MasterUsername="admin",
    MasterUserPassword="your-password",
    VpcSecurityGroupIds=["sg-xxxxxxxx"],
)

instance = response["DBInstance"]
instance_arn = instance["DBInstanceArn"]

waiter = rds.get_waiter("db_instance_available")
waiter.wait(DBInstanceIdentifier=instance["DBInstanceIdentifier"])

print(f"RDS instance created: {instance_arn}")