import boto3
from datetime import datetime, timezone,timedelta

def get_bucket_info():
    s3_client = boto3.client("s3")

    buckets = s3_client.list_buckets()["Buckets"]
    current_date = datetime.now(timezone.utc).astimezone()
    new_buckets = []
    old_buckets = []
    for bucket in buckets:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]
        days_ago_90 = current_date - timedelta(days=90)
        if creation_date < days_ago_90:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return {
        "total_buckets":len(buckets),
        "new_buckets":len(new_buckets),
        "old_buckets":len(old_buckets),
        "new_buckets_names":new_buckets,
        "old_buckets_names":old_buckets
    }

def get_ec2_instances():
    ec2_client= boto3.client("ec2")
    #eu-north-1 :region instead of eu-north-1b
    D={}
    response = ec2_client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
             print("Instance ID:", instance["InstanceId"])

             if "Tags" in instance:
                 for tag in instance["Tags"]:
                     D.update({tag['Key'] : tag['Value']})
                     print(f"{tag['Key']} : {tag['Value']}")
    return D
    # print(type(response))

print(get_ec2_instances())