import boto3
from pprint import pprint
from boto3.dynamodb.conditions import Key


def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movie')

    response = table.query(
        KeyConditionExpression = Key('year').eq(year)
    )

    return response['Items']

if __name__ == "__main__":
    movies_returned = query_movies(2013)

    if movies_returned:
        for movie in movies_returned:
            pprint(movie['title'])
            x = input()