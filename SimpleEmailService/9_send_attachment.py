import boto3

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_attachment():
    msg = MIMEMultipart()

    msg["Subject"] = "This is python with boto3 course"
    msg["From"] = "andythomas.py@gmail.com"
    msg["To"] = "andythomasdotpy@gmail.com"

    body = MIMEText("AWS with Python and Boto3, Thank you for buying")
    msg.attach(body)

    filename = "sample.pdf"

    with open(filename, "rb") as file:
        part = MIMEApplication(file.read())
        part.add_header("Content-Disposition",
                        "attachment",
                        filename=filename)

    msg.attach(part)

    client = boto3.client('ses')

    response = client.send_raw_email(
        Source='andythomas.py@gmail.com',
        Destinations=[
            'andythomasdotpy@gmail.com',
        ],
        RawMessage={
            'Data': msg.as_string()
        },
    )

    print(response)


send_email_attachment()