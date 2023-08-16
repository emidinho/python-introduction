import requests

print()
#api for listing users
response = requests.get("https://reqres.in/api/users")
print(response)
print(response.json())

print()
#api for listing a single user
response = requests.get("https://reqres.in/api/users/5")
print(response)
print(response.json())

print()
#creating user
result = requests.post("https://reqres.in/api/users", {
    "name": "dasco",
    "job": "cloud engineer"
})

print(result)
print(result.json())
print()

#api for putting(update) a single user
response = requests.put("https://reqres.in/api/users/4", {
    "name": "Lino",
    "job": "DevOps Engineer"
})

print(response)
print(response.json())
print()
                  #OR

response = requests.patch("https://reqres.in/api/users/4", {
    "name": "Frank",
    "job": "Solutions Architect"
})

print(response)
print(response.json())
print()

#api for deleting a single user
response = requests.delete("https://reqres.in/api/users/6")
print(response)

