import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('QuizResults')

def lambda_handler(event, context):

    try:
        body = json.loads(event.get('body', '{}'))

        print("Received body:", body)

        name = body.get('name')
        email = body.get('email')
        phone = body.get('phone')
        score = body.get('score')
        correct = body.get('correct')
        wrong = body.get('wrong')
        attempted = body.get('attempted')

        table.put_item(
            Item={
                'email': email,
                'name': name,
                'phone': phone,
                'score': score,
                'correct': correct,
                'wrong': wrong,
                'attempted': attempted,
                'timestamp': str(datetime.now())
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Saved Successfully'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
