import requests
import boto3
ssm_client = boto3.client('ssm')

def get_ssm_parameter(parameter_name):
    response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
    parameter_value = response['Parameter']['Value']
    # print(parameter_value)
    return parameter_value
    

BASE_URL = get_ssm_parameter("BASE_URL")
EXTENSION = get_ssm_parameter("EXTENSION")

print()
#api for updating user utilizing put
def updating_user(user_info, user_id):
    print("updating new user to: ", user_info)
    response = requests.put("{}{}{}".format(BASE_URL,EXTENSION,user_id),user_info)
    print("Response StatusCode: ",response)
    print("Response: ",response.json())    
    
updating_user({
        "name": "dasco",
        "job": "cloud engineer"
}, 4)

print()

updating_user({
    "name": "Lino",
    "job": "DevOps Engineer"
}, 5)

print()

#api for updating user utilizing patch
def updating_user(user_info, user_id):
    print("updating new user to: ", user_info)
    response = requests.patch("{}{}{}".format(BASE_URL,EXTENSION,user_id),user_info)
    print("Response StatusCode: ",response)
    print("Response: ",response.json())

updating_user({
    "name": "Frank",
    "job": "Solutions Architect"
}, 6)

print()

updating_user({
    "name": "Mariia",
    "job": "Secretary"
}, 7)

print()
#api for deleting a single user
def deleting_user(user_id):
    print("deleting user with user_id: ", user_id)
    response = requests.delete("{}{}{}".format(BASE_URL,EXTENSION,user_id))
    print("Response StatusCode: ",response)
    return response

deleting_user(4)
print()
deleting_user(3)
print()
deleting_user(2)
print()
deleting_user(1)
print()
