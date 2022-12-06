import boto3

s3 = boto3.resource('s3')
s3.meta.client.upload_file('/Users/bradleythomas/PycharmProjects/my_site/static/assets/img/avatar_1.jpeg', 'andythomas123', 'avatar.txt')

