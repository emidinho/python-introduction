# copying files from source to destination bucket
import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

s3_client = session.client("s3")

object_list = s3_client.list_objects_v2(
    Bucket='emidinho.net'
    
)

for i in object_list['Contents']:
    print(i ['Key'])
    response = s3_client.copy_object(
        CopySource='emidinho.net/'+ i['Key'],                  # /Bucket-name/Folder_path/filename
        Bucket='emidiobucket',                                 # Destination bucket
        Key=i['Key']                                           # Destination Folder_path/filename
    )                                                          # Destination Folder_path is optional(N/B)

    print(response)




# response = s3_client.copy_object(
#     CopySource='/mybucket/folder1/foo.txt',  # /Bucket-name/path/filename
#     Bucket='mybucket',                       # Destination bucket
#     Key='folder2/foo.txt'                    # Destination Folder_path/filename
                                               # Destination Folder_path is optional(N/B)
# )