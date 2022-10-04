import boto3


def update_username(old_name, new_name):
    # Create IAM client
    iam = boto3.client('iam')

    # Update a user name
    response = iam.update_user(
        UserName=old_name,
        NewUserName=new_name
    )
    print(response)


update_username('newuser1', 'newuser2')
