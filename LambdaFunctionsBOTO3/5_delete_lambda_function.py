import boto3

client = boto3.client('lambda')

response = client.delete_function(
    FunctionName='hello_world_lambda',
)
print(response)