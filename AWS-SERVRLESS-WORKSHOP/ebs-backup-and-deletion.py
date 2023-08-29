import boto3
import time


def lambda_handler(event, context):

    client = boto3.client('ec2')

    response = client.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available'
                ]
            },
        ],
    )

    for i in response["Volumes"]:
        print("current volume info: ", i["VolumeId"])
        print()
        print("creating snapshot for the vol.....", i["VolumeId"])
        response = client.create_snapshot(
            VolumeId = i["VolumeId"]
        )
        time.sleep(10)
        response = client.delete_volume(
        VolumeId = i["VolumeId"]
    )