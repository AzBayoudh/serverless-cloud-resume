import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudResumeTest')

# Increment the views by 1 everytime new viewer
def lambda_handler(event, context):
    response = table.get_item(key={
        'id': '1'
    })
    views = response ['Item']['views']
    views = views + 1
    print(views)
    response = table.put_item(Item={
        'id': '1',
        'views': views
    })    

    return views
        