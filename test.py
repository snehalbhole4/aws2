import json

def lambda_handler(event,context):
    first_name=event['queryStringParameters']['first_name']
    last_name=event['queryStringParameters']['last_name']
    
    
    app_response={}
    app_response['message']='Hello these are the details for ' +first_name+ ' ' + last_name
    app_response['profession']='Software Developer'
    app_response['age']=27
    
    responseObject={}
    responseObject['statusCode']=200
    responseObject['headers']={}
    responseObject['headers']['content-Type']='application/json'
    responseObject['body']=json.dumps(app_response)
    
    
    return responseObject

