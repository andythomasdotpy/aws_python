import boto3

client = boto3.client('ec2')

response = client.create_security_group(
    Description='SecGroupDescription',
    GroupName='SecGroup1Name'
)

print(response)