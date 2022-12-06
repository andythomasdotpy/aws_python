import boto3
from pprint import pprint
import boto3

s3 = boto3.resource('s3')

# client = boto3.client('s3')
#
# response = client.list_buckets()
#
# for bucket in response['Buckets']:
#     print(bucket)


bucket_iterator = s3.buckets.all()

for bucket in bucket_iterator:
    print(bucket.name)