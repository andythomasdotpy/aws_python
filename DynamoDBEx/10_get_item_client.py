import boto3
from pprint import pprint

client = boto3.client('dynamodb')

response = client.get_item(
    TableName='employee',
    Key={
        'emp_id': {
            'S': '3'
        }

    }
)

pprint(response)