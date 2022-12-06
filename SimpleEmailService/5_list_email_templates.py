import boto3

client = boto3.client('ses')

response = client.list_templates()

print(response)