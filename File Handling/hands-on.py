f = open("test1.yml", "r")
# print(f)

# f.write("reviewing file handling. \n" "missed the concept from the start \n")
# f.write("going back to it was quite fun. \n" "i think i got it now." )
print(f.readlines(1))
print(f.read())
f.close


