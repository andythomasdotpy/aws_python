import boto3


def create_login(username, password):

    iam = boto3.client('iam')

    response=iam.create_login_profile(
        UserName=username,
        Password=password,
        PasswordResetRequired=True
    )

    print(response)


create_login('test', 'Aaaaaaaa$')