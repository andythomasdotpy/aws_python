import boto3
from pprint import pprint as pp

db = boto3.client('dynamodb')

response = db.list_tables()

pp(response['TableNames'])