import boto3

db = boto3.resource('dynamodb')

table = db.Table('employee')


with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'emp_id': '4',
            'name': 'John',
            'age': 25,
        }
    )
    batch.put_item(
        Item={
            'emp_id': '5',
            'name': 'Steve',
            'age': 41,
        }
    )