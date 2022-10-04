import boto3


def delete_user_from_group(username):

    iam = boto3.resource('iam')

    group = iam.Group('RDSAdmins')

    response = group.remove_user(
        UserName=username
    )

    print(response)


delete_user_from_group('testuser')