import boto3

client = boto3.client('ses')

response = client.create_template(
    Template={
        'TemplateName': 'mysecondtemplate',
        'SubjectPart': 'Jump',
        'TextPart': 'You might as well jump (jump)',
        'HtmlPart': 'You might as well jump (jump)',
    }
)

print(response)