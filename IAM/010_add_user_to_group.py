import boto3


def add_user_to_group(username, group_name):

    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        GroupName=group_name,
        UserName=username
    )

    print(response)


add_user_to_group('testuser', 'RDSAdmins')