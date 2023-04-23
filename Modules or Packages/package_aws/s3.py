import boto3


def list_all_s3_buckts():
    print("listing all buckets from: ")
    s3_resource=boto3.resource("s3")
    for bucket in s3_resource.buckets.all():
        print(bucket.name) 



