import boto3

session = boto3.session.Session(region_name='us-east-1')

dynamodb =session.resource('dynamodb')

table = dynamodb.Table('jjtech_students')

# print(table.creation_date_time)
# print(table.table_arn)
# print(table.table_size_bytes)
# print(table.item_count)
# print(table.table_status)
# print(table.table_class_summary)
def lambda_handler(event, context):
    print(event)
    response = table.put_item (
                    Item = {
                        'StudentId': '2023aaabb1',
                        'StudentName':'vamsi',
                        "Age":"28",
                        "civil_status":"single",
                        "Country":"india"
                    }
                )
    print("response of item insertion: ", response)
