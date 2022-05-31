import json
import requests

def lambda_handler(event, context):
    
    baseurl = "https://stage.communication-scaffold.oodleslab.com/chat-api/chat/auth/authorize?username=pankaj.raj@oodles.io&password=Dpp@12"
    response = requests.get(baseurl)
    
    if(response.status_code==200):
        api_response = response.json()
        access_token = api_response['access_token']
        print(access_token)
        
        url = "https://stage.communication-scaffold.oodleslab.com/chat-api/v1/management/version"
        headers = {'Authorization': 'Bearer '+ access_token, 'content-type': 'application/json'}
        body = {
            "branchName": "BACKEND103",
            "buildNumber": 2.03,
            "buildType": "FRONTEND",
            "repositoryUrl": "abc.com",
            "revisionNumber": "abcdef",
            "updatedBy": "mansi",
        }    
        rs = requests.post(url, data=json.dumps(body), headers=headers)
        print(rs.status_code)

        responses = requests.post(url, headers=headers, json=body)
        if(responses.status_code==200):
            responses_api = responses.json()
            print(responses_api) 

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
