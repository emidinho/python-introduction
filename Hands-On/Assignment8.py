import requests


BASE_URL = "https://reqres.in"

print()
#api for listing users
def list_users():
    print("Request for list of users...")
    response = requests.get("{}/api/users".format(BASE_URL))
    print("ResponseCode: ",response)
    print("ResponseBody: ",response.json())
    return response.json()

list_users()


print()
#api for listing a single user
def list_user(user_id):
    print("Request for listing a user: ", user_id)
    response = requests.get("{}/api/users/{}".format(BASE_URL,user_id))
    print("ResponseCode: ",response)
    print("ResponseBody: ",response.json())
    return response.json()

list_user(4)
print()
list_user(2)
print()
list_user(6)

print()
#api for creating a single user
def create_user(user_info):
    print("Request for creating a user: ", user_info)
    response = requests.post("{}/api/users".format(BASE_URL), user_info)
    print("ResponseCode: ",response)
    print("ResponseBody: ",response.json())
    return response.json()

create_user({
    "name": "dasco",
    "job": "cloud engineer"
})
print()
create_user({
    "name": "frank",
    "job": "Solutions Architect"
})