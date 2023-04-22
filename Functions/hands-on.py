# print("hi")
# print("jjtech")
# print("pytho")

# def add():
#     sum = 10 + 20
#     print(sum)

# add() 

# def sum(num1, num2):
#     adding = num1 + num2
#     print(adding)

# sum (5000, 4500)
# sum (4000, 4895)


def check_balance(account_number):
    print("current account:", account_number, "current balance:", 1000)


check_balance(145218569814587)


def send_money(amount, receivers_account, account_number):
    current_balance = check_balance(account_number)
    print("receivers account: ", receivers_account, "senders account: ", account_number, "amount transfered: ", amount)


send_money(125463, 145218569814587, 1500)