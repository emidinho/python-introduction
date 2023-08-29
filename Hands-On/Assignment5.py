print("mobile password simulation")
print()
print()

total_attempt = 5

attempt_count = 0

correct_password = 12345

while attempt_count < total_attempt:
    attempt_count = attempt_count + 1
    tried_password = int(input("Enter password: "))

    if tried_password == correct_password:
        print("login successful")
        break

    elif tried_password != correct_password and attempt_count < total_attempt:
        print("try again") 

    else:
        print("phone locked, require PIN to unlock")

