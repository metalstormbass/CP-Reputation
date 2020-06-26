import requests
import json

#remove https warning
requests.packages.urllib3.disable_warnings()

#variables
url = "https://rep.checkpoint.com/rep-auth/service/v1.0/request"

#Authentication
def auth_token(url, client_key):
    headers = {
                'Client-Key': client_key,
            }
    try:
        response = requests.get(url, headers=headers, verify=False)
        #response_json = json.loads(response.content)
        print (response.content)
        #return response_json
    
    except Exception as error:
            print ("Error Occured")
            print (error)
            sys.exit()     
            

#Post Functionality     
def post (token, client_key, json_data):
        headers = {
            'content-type': "application/json",
        }
        
        try:
            response = requests.post(url, json=json_data, headers=headers, verify=False)
            response_json = json.loads(response.content)
            #print (response_json)
            return response_json

        except Exception as error:
            print ("Error Occured")
            print (error)
            sys.exit()     


            
#Main Functionality

client_key = input("Enter your API Key: ")

auth_token(url,client_key)