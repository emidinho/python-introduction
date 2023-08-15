def greeting(name):
    print("hello",name,"!")
    return True

greeting("America")

greeting("Canada")

result = greeting("canada")
print(result)

response = len("ironman")
print(response)

def validate_accont(account_number):
    print("validating account: ", account_number)
    print("connecting to database...")
    print("verifying the account: ", account_number)
    print("valid account")
    return True

valid_acc = validate_accont(123456789)
print(valid_acc)