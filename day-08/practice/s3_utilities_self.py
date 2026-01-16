import boto3
import os

class AWSUtils :
    def __init__(self):
           self.s3=self.get_connections("s3")
        #    self.ec2=self.get_connections("ec2")
    def get_connections(self,service):
        return boto3.client(service) # creating a client for access s3 services
    #client and server : apis call/
    # client calls server
    def show_buckets(self):
        self.response=self.s3.list_buckets()
        for bucket in self.response["Buckets"]:
            print(bucket["Name"])

    def create_buckets(self, bucket_name):
            self.response=self.s3.create_bucket(Bucket=bucket_name)
            if self.response["ResponseMetadata"]["HTTPStatusCode"] == 200:
             print("New S3 Bucket is created.")
            else:
                print("error has occured")

    def delete_bucket(self, bucket_name):
        try:
            self.response = self.s3.delete_bucket(Bucket=bucket_name)
            print("Mentioned S3 Bucket is deleted.")
        except:
            print("unable to delete,error has occured")

    # def show_regions(self):
    #     self.response=self.ec2.describe_regions()

    def upload_files (self,filepath , bucket_name, key_name):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join( self.base_dir, filepath)
        self.response=self.s3.upload_file( self.file_path, bucket_name, key_name)
        print("all good")

if __name__== "__main__":
    aws= AWSUtils()
    aws.show_buckets()
    # s3=get_connections("s3")
    # ec2=get_connections("ec2")
    # show_buckets(s3)
    # create_buckets(s3,"tgbps----bucket")
    # delete_bucket(s3, "rehman890" )
    aws.upload_files('app.log_otput.json', 'tgbpsbucket',"hello3")