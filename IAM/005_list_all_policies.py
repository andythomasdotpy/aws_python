import boto3


def list_poliies():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="Local"):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            arn = policy['Arn']

            print(f"policy name:  {policy_name}, Arn = {arn}")


list_poliies()