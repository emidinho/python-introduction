import boto3

session = boto3.session.Session(region_name="us-east-1")

ec2_client = session.client('ec2')

def lambda_handler(event, context):
    vol_response = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available',
                ]
            },
        ]
    )

    print(vol_response)

    for i in vol_response['Volumes']:
        print("current available ebs vol:",i['VolumeId'])
        response = ec2_client.delete_volume(
            VolumeId=i['VolumeId'],
            DryRun=False
        )
        print("delete operation:",response)




