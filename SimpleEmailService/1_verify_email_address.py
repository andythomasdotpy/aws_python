import boto3

client = boto3.client('ses')

response = client.verify_email_address(
    EmailAddress='andythomasdotpy@gmail.com'
)

print(response)