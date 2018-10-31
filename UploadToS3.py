import boto3
import os


os.environ['AWS_SHARED_CREDENTIALS_FILE'] ='credentials.txt'

boto3.setup_default_session(region_name='us-east-2')

# ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# print(response)

s = boto3.resource('s3')
for a in s.buckets.all():
    print(a.name)
       
#s.create_bucket(Bucket='mohitsaxena2005-bms-mohitsaxena2005')

# s3=boto3.resource('s3')
# s3.create_bucket(Bucket='testfromcmdline2005678945636r36r236823356747425379237')
s.Object('mohitsaxena2005-bucket-bms', 'movieInfo_2018-10-3115_00_00.csv').put(Body=open('movieInfo_2018-10-3115_00_00.csv', 'rb'), ACL='public-read')


