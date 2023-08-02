# marks = 80
marks = int(input("enter you grade: "))


if marks >= 75 and marks <= 80:
    print("Passed. Grade C")
elif marks >=81 and marks <=85:
    print("Passed. Grade C+")
elif marks >=86 and marks <=90:
    print("Passed. Grade B")
elif marks >=91 and marks <=95:
    print("Passed. Grade B+")
elif marks >=96 and marks <=100:
    print("Passed. Grade A")
else:
    print("FAILED")
