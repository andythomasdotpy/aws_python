import boto3
from pprint import pprint

client = boto3.client('ses')

response = client.get_template(
    TemplateName='myfirsttemplate'
)

pprint(response['Template'])