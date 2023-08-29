import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

client = session.client('s3')

response = client.list_buckets()

for i in response["Buckets"]:
    print(i["Name"])

print(response["ResponseMetadata"]["HTTPHeaders"]["date"])
print(response["ResponseMetadata"]["HTTPHeaders"]["server"])
print(response["ResponseMetadata"]["HTTPHeaders"]["x-amz-request-id"])