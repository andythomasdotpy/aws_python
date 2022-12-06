import boto3

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')

with open('lambda.zip', 'rb') as f:
    zipped_code = f.read()

role = iam_client.get_role(RoleName='PYLamdaBasicExecution')

response = lambda_client.create_function(
    FunctionName='hello_world_lambda',
    Runtime='python3.9',
    Role=role['Role']['Arn'],
    Handler='lambda_function.lambda_handler',
    Code=dict(ZipFile=zipped_code),
    Timeout=300
)

print(response)