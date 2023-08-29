import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

client = session.client('ec2')

response = client.describe_instances()
response1 = client.describe_regions()

print(response["Reservations"][0]["Instances"][0]["InstanceId"])
# print(response1)

# for i in response1["Regions"]:
#     print(i["RegionName"])