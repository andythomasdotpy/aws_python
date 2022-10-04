import boto3


def detach_policy(policy_arn, username):

    iam = boto3.client('iam')

    response = iam.detach_user_policy(
        UserName=username,
        PolicyArn=policy_arn

    )

    print(response)


detach_policy('arn:aws:iam::aws:policy/AmazonRDSFullAccess', 'testuser2')