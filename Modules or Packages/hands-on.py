# import uuid
# import calendar
# import os

# print(uuid.uuid4())
# print(os.getcwd())
# print(calendar.isleap(2023))
# print(calendar.weekday(2023,4,24))
# file_size = os.path.getsize("jj-tech-student.tf")
# print(file_size, "bytes")

from CommonsModule import commons
from package_aws import s3


f=commons.check_if_valid_account(123456789123)
print(f)

g=s3.list_all_s3_buckts()
print(g)