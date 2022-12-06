import boto3

db = boto3.resource('dynamodb')
table = db.Table('movie')

response = table.get_item(
    Key={
        'emp_id': '2013'
    },
)

print(response)