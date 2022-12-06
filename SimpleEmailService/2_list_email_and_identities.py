import boto3

client = boto3.client('ses')

response = client.list_identities(
    IdentityType='EmailAddress',

)

print(response['Identities'])