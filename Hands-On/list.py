# fruits = ["oranges","grapes","mangoes","lemons","tangerines","banana"]

# students = ["james","jake","sony","bob","virj","mariia"]

# speeds = [0,20,40,60,80,100]

# custom_list = ["emidio",15,50.4,True,None]

# print(students)
# print("lemons" in fruits)
# print(speeds)
# print(custom_list)

# print(type(students))
# print(type(fruits))
# print(type(speeds))
# print(type(custom_list))

# print(len(students))
# print(len(fruits))
# print(len(speeds))
# print(len(custom_list))

# print(fruits[0])
# print(fruits[0:])
# print(fruits[0:3])
# print(students[1])
# print(students[1:])
# print(students[1:4])


# print(dir(fruits))

# students.reverse()
# print(students)

fruits = ["kiwi", "grapes", "apple", "orange", "banana", "strawberry", "watermelon", "pineapple", "mango", "pear"]


print(fruits)

fruits.sort(reverse=False)
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.reverse()
print(fruits)  

fruits.append("zanziba")
print(fruits)

x= fruits.index("mango")
print(x)
# or
print(fruits.index("mango"))

fruits.remove("banana")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.insert(1, "orange")
print(fruits)

fruits[4] = "limes"  #(replacing orange with lime)
print(fruits[0:])

new_fruits = ['blueberry', 'cherry', 'blackberry']
fruits.extend(new_fruits)
print(fruits)

x = fruits.count("cherry")
print(x)
# or
print(fruits.count("cherry"))

x = fruits.copy()
print(x)
# or
print(fruits.copy())

for each_fruit in fruits:
    print(each_fruit)

fruits.clear()
print(fruits)

