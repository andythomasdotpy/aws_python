import boto3


def add_user_to_group(group_name, policy_arn):

    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )

    print(response)


add_user_to_group('RDSAdmins', 'arn:aws:iam::aws:policy/AmazonRDSFullAccess')