import boto3
from pprint import pprint as pp

db = boto3.resource('dynamodb')

response = db.batch_get_item(
    RequestItems={
            'employee': {
                'Keys': [
                    {
                        'emp_id': '2'
                    },
                    {
                        'emp_id': '1'
                    }
                ]
            },
            'Article': {
                'Keys': [
                    {
                        'id': 2,
                        'pub_date': '2022-10-02'
                    }
                ]
            }
    }
)

pp(response['Responses'])