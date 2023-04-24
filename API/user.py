import requests

API_END_POINT = "https://reqres.in"

# response = requests.get("https://reqres.in/api/users")
# print("ResponseCode: ", response.status_code)

# print("ResponseCode: ", response.json())

# print()

# response = requests.get("https://reqres.in/api/users/4")
# print("ResponseCode: ", response.status_code)

# print("ResponseCode: ", response.json())

# print()


# response = requests.post("https://reqres.in/api/users", json={
#     "name": "jurgen",
#     "job": "coach"
# })
# print("ResponseCode: ", response.status_code)

# print("ResponseCode: ", response.json())


# def get_all_users():
#     print("getting all users:")
#     response = requests.get(API_END_POINT + "/api/users")
#     print("ResponseCode: ", response.status_code)
#     print("ResponseCode: ", response.json()) 


# get_all_users()


def get_user (user_id):
    print("getting individual user:", user_id)
    response = requests.get(API_END_POINT + "/api/users/" + str(user_id))
    print("ResponseCode: ", response.status_code)
    print("ResponseCode: ", response.json())

get_user(5)

# def create_user(user_data):
#     print("Creating a user:", user_data)
#     response = requests.post(API_END_POINT + "/api/users", json=user_data)
#     print("ResponseCode: ", response.status_code)
#     print("ResponseCode: ", response.json())


# create_user({
#     "name": "pep",
#     "job": "Assistant coach"
# })