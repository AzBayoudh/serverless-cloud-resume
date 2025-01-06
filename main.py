import json
import boto3

# Initialize DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudResumeTest')

# Lambda handler function
def lambda_handler(event, context):
    try:
        # Get the item from DynamoDB
        response = table.get_item(Key={'id': '1'})

        # Check if the item exists
        if 'Item' in response:
            views = response['Item'].get('views', 0)  # Default to 0 if 'views' doesn't exist
        else:
            # Initialize the item if it doesn't exist
            views = 0
        
        # Increment the views
        views += 1
        
        # Update the item in DynamoDB
        table.put_item(Item={
            'id': '1',
            'views': views
        })

        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Views updated', 'views': views})
        }

    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
