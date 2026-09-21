import os
from dotenv import load_dotenv

import boto3

load_dotenv()
AWS_USER_KEY=os.getenv('AWS_USER_KEY')
AWS_USER_SECRET=os.getenv('AWS_USER_SECRET')
AWS_REGION=os.getenv('AWS_REGION')
AWS_TABLE_NAME=os.getenv('AWS_TABLE_NAME')

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status:", table.table_status)
