from AWS import rds,s3,ec2
from math import sqrt

print(pow(5,10))
result = sqrt(144)
print(result)

print("user creation process...")
rds.insert_data("emidio", "admin@admin.com" , 12345)
s3.upload_profile_pic("ocean")
ec2.stop_ec2_instance("id-145623987896")