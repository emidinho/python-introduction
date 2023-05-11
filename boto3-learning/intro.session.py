import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

# s3 = session.client("s3")
# rds = session.client("rds")
ec2 = session.client("ec2")

#launching an ec2 instance with boto3

# response = ec2.run_instances(
#     BlockDeviceMappings=[
#         {
#             'DeviceName': '/dev/xvda',
#             'Ebs': {

#                 'DeleteOnTermination': True,
#                 'VolumeSize': 8,
#                 'VolumeType': 'gp2'
#             },
#         },
#     ],
#     ImageId='ami-03c7d01cf4dedc891',
#     InstanceType='t2.micro',
#     MaxCount=3,
#     MinCount=1,
#     KeyName='linux-keypair',
#     SubnetId='subnet-01345df02fbb7abcb',
#     UserData='''
#           #!/bin/bash
#           sudo su
#           yum update -y
#           yum install -y httpd.x86_64
#           systemctl start httpd.service
#           systemctl enable httpd.service
#           echo "launching an instance through python" >> /var/www/html/index.html
#           ''',
#     Placement={
#         'AvailabilityZone': 'us-east-1a',
#         'Tenancy': 'default'
#     },
#     IamInstanceProfile={
#         'Name': 'EC2-AmazonS3ReadOnlyAccess'
#     },
#     Monitoring={
#         'Enabled': False
#     },
#     SecurityGroupIds=[
#         'sg-047d5bd78600371c7',
#     ],
#     TagSpecifications=[
#         {
#             'ResourceType': 'instance',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value': 'server-boto3'
#                 },
#             ]
#         },
#     ],
# )

# print(response)


#terminating an ec2 instance with boto3
# response_terminate = ec2.terminate_instances(
#     InstanceIds=[
#         'i-00e64c5d4f0c3f913', 'i-02c6966aafdd4baf1'
#     ],
#     DryRun=False
# )

# print(response_terminate)


#stopping an ec2 instance with boto3
# The valid values for instance-state-code will all be in the range of the low byte and they are:
# 0 : pending
# 16 : running
# 32 : shutting-down
# 48 : terminated
# 64 : stopping
# 80 : stopped

# response_stop = ec2.stop_instances(
#     InstanceIds=[
#         'string',
#     ],
#     Hibernate=False,
#     DryRun=False,
#     Force=False
# )

# print(response_stop)



#starting an ec2 instance with boto3
# response_start = ec2.start_instances(
#     InstanceIds=[
#         'string',
#     ],
#     DryRun=False
# )

# print(response_start)

