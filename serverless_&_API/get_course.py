import boto3

session = boto3.session.Session(region_name="us-east-1")

dynamodb = session.resource('dynamodb')

table = dynamodb.Table('courses_table')

# print(table)
# print(table.item_count)
# print(table.table_id)
# print(table.table_arn)
# print(table.creation_date_time)

# print(table.scan())
def lambda_handler(event, context):
    response = table.get_item(
        Key={
            "CourseId":"1"
        }
    )
    print("obtained item: ",response['Item'])

