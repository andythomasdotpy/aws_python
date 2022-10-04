import boto3

def list_users():
    iam = boto3.client('iam')

    # List users with the pagination interface
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        print(response)
        print()
        print()
        for user in response['Users']:
            username = user['UserName']
            arn = user['Arn']
            print(f"UserName: {username} Arn: {arn}")

list_users()