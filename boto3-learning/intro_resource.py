import boto3

iam_resource = boto3.resource("iam")

policy_iterator = iam_resource.policies.all()

print(policy_iterator)