import boto3

s3 = boto3.resource('s3')

bucket = s3.create_bucket(
    Bucket='pythonresbucket5555',
    ACL='public-read',
)