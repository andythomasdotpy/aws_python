import boto3


def send_email_text():
    client = boto3.client('ses')
    CHARSET = 'UTF-8'

    response = client.send_email(
        Source='andythomas.py@gmail.com ',
        Destination={
            'ToAddresses': [
                'andythomasdotpy@gmail.com',
                'andythomas.py@gmail.com'
            ],
        },
        Message={
            'Subject': {
                'Data': 'Custom Subject',
                'Charset': CHARSET
            },
            'Body': {
                'Text': {
                    'Data': 'My custom data body.',
                    'Charset': CHARSET
                },
            }
        },
    )

    print(response)


send_email_text()