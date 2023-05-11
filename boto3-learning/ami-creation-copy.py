import boto3
import time


session = boto3.session.Session(profile_name="default", region_name="us-east-1")

ec2_client = session.client('ec2')

instances = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'prod1', 
            ]
        },
    ]
)

images_list = []

for i in instances['Reservations']:
    # print(i['Instances'][0]['InstanceId'])
    for j in i['instances']:
        print(j['instanceId'], j['Tags'][0]['Value'])
        response = ec2_client.create_image(
            InstanceId=j['instanceId'],
            Name=j['Tags'][0]['Value']
        )
        print(response)
        images_list.append(response['ImageId'])


time.sleep(280)

for image in images_list:    
    copy_response = ec2_client.copy_image(
        Description='copy_exmaple',
        Name='image',
        SourceImageId='image',
        SourceRegion='us-east-1'
    )
    print(copy_response)

