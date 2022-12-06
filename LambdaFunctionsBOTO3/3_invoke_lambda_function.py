import boto3
import json

lambda_client = boto3.client('lambda')

test_event = dict()

response = lambda_client.invoke(
    FunctionName="hello_world_lambda",
    Payload=json.dumps(test_event)
)

# print(response['Payload'])
# print(response['Payload'].read())
print(response['Payload'].read().decode('utf-8'))

# b'{"statusCode": 200, "body": "\\"Hello from Python and Boto3\\""}'
