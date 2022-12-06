import boto3

client = boto3.client('ec2')

response = client.authorize_security_group_ingress(
    GroupId='sg-076b613380495c012',
    IpPermissions=[
        {
            'FromPort': 80,
            'ToPort': 80,
            'IpProtocol': 'TCP',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'MyDescription'
                }
            ]
        },
{
            'FromPort': 22,
            'ToPort': 22,
            'IpProtocol': 'TCP',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'MyDescription'
                }
            ]
        }
    ]
)

print(response)