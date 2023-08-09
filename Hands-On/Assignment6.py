def validate_card(card_number, pin_number, exp_date, CCV):
    print("validating card with: ", card_number)
    print("calling DB to validate: ", card_number,pin_number,exp_date,CCV)


print("payment via POS")
validate_card(1234567890, 456789, "2029-09", 987)

print("payment via online")
validate_card(987654321, 987654, "2030-12", 123)


def withdraw_money(amount, card_number, pin_number, exp_date, CCV):
    print("withdrawing a total of: ", amount)
    validate_card(card_number, pin_number, exp_date, CCV)

withdraw_money(5000, 1237890456, 458967, "2039-10", 456)