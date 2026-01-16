import boto3
import boto3.session

def AWSUtils():
    s3_client=boto3.client("s3")
    response=s3_client.list_buckets()
    # print(type(response))
    buckets=[]
    #
    for bucket in s3_client.list_buckets()["Buckets"]:
            buckets.append(bucket["Name"])
    print (buckets)

AWSUtils()
#client : s3 .ec2 etc
