import boto3

cf_client = boto3.client('cloudformation')

with open('DynamoDB.yaml', 'r') as file:
    db_template = file.read()
    # print(db_template)

params = [
    {
        'ParameterKey': 'HashKeyElementName',
        'ParameterValue': 'EmployeeID'
    }
]

response = cf_client.create_stack(
    StackName="dynamostacknew",
    TemplateBody=db_template,
    Parameters=params
)

print(response)
