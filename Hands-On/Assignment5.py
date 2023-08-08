print("mobile password simulation")
print()
print()

total_attempt = 5

attempt_count = 0

correct_password = 12345

while attempt_count < total_attempt:
    attempt_count = attempt_count + 1
    tried_password = int(input("Enter password :"))

    # if attempt_count == total_attempt and correct_password != 12345:
    #     print("phone blocked")

    if correct_password == tried_password:
        print("login successful")
        break

    else:
        print("try again")

    
    # print("enter password", attempt_count)

