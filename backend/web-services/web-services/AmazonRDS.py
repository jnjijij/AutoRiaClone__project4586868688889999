import boto3
from sqlalchemy.dialects.postgresql import psycopg2

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
conn = psycopg2.connect(
    dbname='your-db-name',
    user='your-user-name',
    password='your-password',
    host='your-host-name',
    port='your-port-number'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM your_table')

rows = cursor.fetchall()
for row in rows:
    print(row)

print(f"RDS instance created: {instance_arn}")