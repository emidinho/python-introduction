# print (1)
# print (100*500)
# print ("i'm learning python basics")
# print ("emidio is almost a geek")


# a = 2
# if a == 2: 
#     print ('a is 2')
# if a % 2 == 0:
#     print ('a is even')  

# def one():
#     print("one")

# def two():
#     print("two")

# def three():
#     print("three")

# if __name__ == '__main__':
#     one()

import boto3

def get_instances():
    instance_id=[]
    resource = boto3.resource('ec2')
    for i in resource.instances.all():
        instance_id.append(i.id)
    return instance_id

def get_ebs_volumes():
    ebs_list=[]
    resource = boto3.resource('ec2')
    for v in resource.volumes.all():
        ebs_list.append(v.id)
    return ebs_list

def create_tags(instanceids):
    client = boto3.client('ec2')
    response = client.create_tags(
        Resources=instanceids,
        Tags=[
            {
                'Key': 'Company',
                'Value': 'JJTech'
            },
            {
                'Key': 'Name',
                'Value': 'TestInstancesBoto3'
            },
        ]
    )

def lambda_handler(context, event):
    instanceids=get_instances()
    print(instanceids)
    create_tags(instanceids)
    ebs_volume_ids=get_ebs_volumes()
    create_tags(ebs_volume_ids)

lambda_handler()