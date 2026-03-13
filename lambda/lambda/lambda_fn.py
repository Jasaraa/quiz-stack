import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('QuizResults')

def lambda_handler(event, context):

    # Handle CORS preflight request
    if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps("CORS OK")
        }

    body = json.loads(event['body'])

    table.put_item(
        Item={
            'email': body['email'],
            'name': body['name'],
            'phone': body['phone'],
            'score': body['score'],
            'attempted': body['attempted']
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps("Quiz saved successfully")
    }
