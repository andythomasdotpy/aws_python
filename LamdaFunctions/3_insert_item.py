import boto3


def lambda_handler(event, context):
    db = boto3.resource('dynamodb')

    table = db.Table('Users1')

    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                'id': 1,
                'name': 'andy',
                'age': '20'
            }
        )

        batch.put_item(
            Item={
                'id': 2,
                'name': 'bill',
                'age': '23'
            }
        )