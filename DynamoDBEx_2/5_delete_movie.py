import boto3
from pprint import pprint
from botocore.exceptions import ClientError


def delete_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movie')

    try:
        response = table.delete_item(
            Key={
                'year': year,
                'title': title,
            }
        )

    except ClientError as e:
        print(e.response['Error']['Message'])

    else:
        return response


if __name__ == "__main__":
    delete_response = delete_movie("The Avengers", 2012)

    if delete_response:
        pprint(delete_response)