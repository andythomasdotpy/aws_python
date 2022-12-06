import boto3
from pprint import pprint as pp

db = boto3.client('dynamodb')

#Add Backup
"""
response = db.create_backup(
    TableName='Article',
    BackupName='article_backup'
)

pp(response)
"""

#Delete Backup
response = db.delete_backup(
    BackupArn='arn:aws:dynamodb:us-east-1:528336348428:table/Article/backup/01665181287395-98c71767'
)
pp(response)