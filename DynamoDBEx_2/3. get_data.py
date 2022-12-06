import boto3
from pprint import pprint

def get_data(title, year):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movie')

    response = table.get_item(
        Key={
            'title': title,
            'year': year
        }
    )

    return response['Item']

pprint(get_data('Hercules', 1997))