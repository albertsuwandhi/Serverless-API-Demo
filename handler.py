import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('usersTable')

def readDynamoDB(event, context):
    #body = {
    #    "message": "Go Serverless v1.0! Your function executed successfully!",
    #    "input": event
    #}
    
    response = table.scan()
    data = {'Count':response['Count'],'Items':response['Items']}

    response = {
        "statusCode": 200,
        "body": json.dumps(data)
        
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration

    #return {
    #    "message": "Go Serverless v1.0! Your function executed successfully!",
    #    "event": event
    #}
