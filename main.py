import json
import boto3

# Initialize DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudResumeTest')

# Lambda handler function
def handler(event, context):
    response = table.get_item(
        key ={'id': '1'}
    )

    views = response['item']['views'] 
    views += 1
    print(views)

    response = table.put_item(
        key ={'id': '1',
              'views': views}

    )

    return views

