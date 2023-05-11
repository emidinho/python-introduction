import boto3

iam_resource = boto3.resource("iam")

# print(iam_resource)### gives the aws resources that respond to resources

policy_iterator = iam_resource.policies.all()

# print(policy_iterator)

# for i in policy_iterator:
#     print(i)

for i in policy_iterator:
    if i.policy_name == "AmazonEC2FullAcess":
        print(i.policy_name, i.create_date, i.policy_id)
        i.attach_user(UserName="emidio")





