import boto3

def send_html_email():
    client = boto3.client('ses')
    CHARSET = 'UTF-8'

    html_email_content = """
        <html>
            <head></head>
            <h1 style='text_align:center'>AWS with Python and Boto3</h1>
            <p style='color:red'>Welcome to the course and thank you!</p>
        </html>
    """

    response=client.send_email(
        Source='andythomas.py@gmail.com',
        Destination={
            'ToAddresses': [
                'andythomas.py@gmail.com',
                'andythomasdotpy@gmail.com'
            ],
        },
        Message={
            'Subject': {
                'Data': 'HTML Subject Email',
                'Charset': CHARSET
            },
            'Body': {
                'Html': {
                    'Data': html_email_content,
                    'Charset': CHARSET
                }
            }
        },
    )


    print(response)


send_html_email()