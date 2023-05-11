import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

ec2_client = session.client('ec2')

