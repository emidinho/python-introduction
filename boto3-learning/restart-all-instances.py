import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

ec2 = boto3.resource('ec2')

#get only running instances
instances = ec2.instances.filter(
    Filters=[{'Name':'instance-state-name', 'Values':['stopped']}]
)

#stop instances
for instance in instances:
    instance.start()
    print('restarted instances: ', instance.id)