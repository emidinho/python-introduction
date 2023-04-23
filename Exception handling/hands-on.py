# print("heyyy, this is emi")
# try:
#     marks = 95
#     print(marks/0)

#     print("hlo jj")
#     print("learning pytho")
# except Exception as e:
#     print("unexpected error", e)

# print("complete")


# def add(num1, num2):
#     try:
#         total = num1 + num2
#         print(total) 
#         return total
#     except Exception as e:
#         print(e, num1, num2)



# add (500, 200)
# add (458, "589")
# add (257, 158)

try:
    f=open("jj-tech-students", "w")
    f.write("\n new doc", "\n all the way up")
except Exception as e:
    print("hello",e)
    f=open("jj-tech-student.tf", "x")
finally:
    print("closing file")
    f.close()

