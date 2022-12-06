import boto3
from pprint import pprint


client = boto3.client('ec2')

response = client.create_key_pair(
    KeyName='mykey1',
    KeyType='rsa'
)

pprint(response['KeyMaterial'])


f = open("mykey.pem", "w")
f.write(response['KeyMaterial'])
f.close()