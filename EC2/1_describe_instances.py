import boto3
from pprint import pprint

client = boto3.client('ec2')

response = client.describe_instances()

pprint(response)