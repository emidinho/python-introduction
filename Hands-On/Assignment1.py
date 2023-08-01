email = "emidio.alemnju@jjtech.com"  #extract jjtech (company name)

data = email.split("@")

print(data)

company_name = data[1].split(".")

print(company_name)

outcome = company_name[0]

print(outcome)