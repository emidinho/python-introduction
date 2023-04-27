import boto3

# boto3.resource("s3")
s3_client = boto3.client("s3")

# list_bucket_response = s3_client.list_buckets()
# print(list_bucket_response)

# put_object_response=s3_client.put_object(
#     Body="C:\\Users\\ALEMNJU EMIDIO\\Desktop\\python-practice\\boto3-learning\\s3_python_test.yml", 
#     Bucket="emidiobucket1", 
#     Key="test")
# print(put_object_response)

s3 = s3_client
with open('C:\\Users\\ALEMNJU EMIDIO\\Desktop\\python-practice\\boto3-learning\\s3_python_test.yml', 'rb') as data:
    s3.upload_fileobj(data, 'emidiobucket', 's3_python_test.yml')
    print(s3.upload_fileobj) 

