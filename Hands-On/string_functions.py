name = "emidio"

name1 = "SPIDERMAN"

username = "       lino        "

print(name.upper())

print(name1.lower())

print(name1.replace("SPIDER", "IRON"))

print(username)
print(len(username))


print(username.lstrip())
print(username.rstrip())

new_username = username.strip()
print(len(new_username))



message = "hello everyone how are you"

print(message.split())

message = "hello everyone, how are you"

print(message.split(","))

message = "hello, everyone, how are you"

print(message.split(","))


mail = "admin@gmail.com"

print(mail.split("@"))