import boto3


def add_user_to_group(username):

    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)


add_user_to_group('testuser')