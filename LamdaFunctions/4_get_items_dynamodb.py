import boto3


def lambda_handler(event, context):
    db = boto3.resource('dynamodb')

    response = db.batch_get_item(
        RequestItems={
            'Users1': {
                'Keys': [
                    {
                        'id': 1
                    }
                ]
            },
        }
    )

    print(response)