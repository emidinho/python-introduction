emails = [
    "vamsi@jjtech.com", 
    "ironman@amazon.com",
    "hulk@accenture.com",
    "spiderman@microsoft.com",
    "captain.america@google.com"
]

#extract company names

companies = []

for i in emails:
    #print(i)
    data = i.split("@")
    #print(data)
    data1 = data[1].split(".")
    #print(data1)
    data2 = data1[0]
    
    companies.append(data2)

print(companies)