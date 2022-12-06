import boto3
from decimal import Decimal
from pprint import pprint


def update_movie(title, year, rating, plot, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movie')

    response = table.update_item(
        Key={
            'year': year,
            'title': title,
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues={
            ':r':Decimal(rating),
            ':p':plot,
        },
        ReturnValues="UPDATED_NEW"
    )

    return response


updated_movie = update_movie(
    "Rush", 2013, 1, "My new plot summary")

pprint(updated_movie)
