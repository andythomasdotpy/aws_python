import boto3
from pprint import pprint

client = boto3.client('cloudformation')

response = client.describe_stacks(
)

pprint(response)