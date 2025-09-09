import json
import os
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # TODO: Implement your get alias prompt logic here
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from get-alias-promt',
            'table': table_name
        })
    }