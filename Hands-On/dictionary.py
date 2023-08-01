student1 = {"name": "joe","gender": "male","country": "US","age": 25}

student2 = {"name": "mariia","gender": "female","country": "Ukraine","age": 19}

student3 = {"name": "mark","gender": "male","country": "canada","age": 55}

print(student1)

print(student3)

print(type(student1))

print(len(student1))

print(student1["name"])

print(student3["gender"])

print(student2["country"])

student3["name"] = "emidio"
student3["age"] = 28
print(student3)

student2["results"] = True

print(student2)

student3["hobbies"] = ["reading", "writing"]

print(student3)

student3.pop("age")
print(student3)

print(student3.keys())
print(student3.values())

for i in student3.values():
    print(i)

for x in student3["hobbies"]:
    print(x)

print(student3.items())

for key, val in student3.items():
    print(key, val)
    


##FACT ABOUT LIST. 1) MUTABLE(UPDATABLE) 