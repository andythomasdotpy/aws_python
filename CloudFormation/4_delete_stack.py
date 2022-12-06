import boto3
from pprint import pprint

client = boto3.client('cloudformation')

response = client.delete_stack(
    StackName='DynamoDBStack',
)

print(response)