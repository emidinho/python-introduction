# name = "pytho workshop"

# for each_character in name:
#     print(each_character)


# fruits = ["apple", "orange", "grapes", "mangoes", "lemons"]



marks = [63,77, 23,97,98,85,95,80, 87,93]
print("\n grading system ")

for x in marks:
    print(x)
    if x >= 75 and x <= 80:
        print("Passed: C")
    elif x >= 81 and x <= 85:
        print("Passed: B-")
    elif x >= 86 and x <= 90:
        print("Passed: B")
    elif x >= 91 and x <= 94:
        print("Passed: B+")
    elif x >= 95 and x <= 97:
        print("Passed: A")
    elif x >= 98 and x <= 100:
        print("Passed: A+")    
    else:
        print("Failed")

