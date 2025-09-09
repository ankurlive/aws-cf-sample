import json
import os
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # TODO: Implement your feedback collection logic here
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from feedback_collection',
            'table': table_name
        })
    }