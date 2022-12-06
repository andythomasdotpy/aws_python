import boto3

client = boto3.client('ses')

response = client.send_templated_email(
    Source='andythomas.py@gmail.com',
    Destination={
        'ToAddresses': [
            'andythomasdotpy@gmail.com',
        ],
    },

    Template='myfirsttemplate',
    TemplateData='{"replace": "value"}'
)

print(response)