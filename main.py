import requests
import sys
import json
from termcolor import colored, cprint 


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
        #print (response.content)
        return response.content
    
    except Exception as error:
            print ("Error Occured")
            print (error)
            sys.exit()     
            

#Post Functionality     
def post (token, client_key, resource, res_type):
    
    rep_url = "https://rep.checkpoint.com/"+res_type+"-rep/service/v2.0/query?resource="+resource
    
    json_data = {
    "request": [{
        "resource": resource
    }]
       }
    
    headers = {
                'content-type': "application/json",
                'Client-Key': client_key,
                "token" : token
            }
        
    try:
        rep_response = requests.post(rep_url, json=json_data, headers=headers, verify=False)
        rep_response_json = json.loads(rep_response.content)
        
        status = rep_response_json['response'][0]['reputation']['classification']   
        print (json.dumps(rep_response_json, indent=4, sort_keys=True))
        
        print ("\n")
        if status == "Benign":
            print ("The resource "+resource+" is:")
            cprint(status, 'green', attrs=['bold'], file=sys.stderr) 
        else: 
            print ("The resource "+resource+" is:")
            cprint(status, 'red', attrs=['bold'], file=sys.stderr) 
        print ("\n")

    except Exception as error:
        
        print ("Error Occured")
        print (error)
        sys.exit()     
                        
            
#Title 
print ('''
                                                                                                 
 @@@@@@@  @@@  @@@  @@@@@@@@   @@@@@@@  @@@  @@@     @@@@@@@    @@@@@@   @@@  @@@  @@@  @@@@@@@  
@@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@     @@@@@@@@  @@@@@@@@  @@@  @@@@ @@@  @@@@@@@  
!@@       @@!  @@@  @@!       !@@       @@!  !@@     @@!  @@@  @@!  @@@  @@!  @@!@!@@@    @@!    
!@!       !@!  @!@  !@!       !@!       !@!  @!!     !@!  @!@  !@!  @!@  !@!  !@!!@!@!    !@!    
!@!       @!@!@!@!  @!!!:!    !@!       @!@@!@!      @!@@!@!   @!@  !@!  !!@  @!@ !!@!    @!!    
!!!       !!!@!!!!  !!!!!:    !!!       !!@!!!       !!@!!!    !@!  !!!  !!!  !@!  !!!    !!!    
:!!       !!:  !!!  !!:       :!!       !!: :!!      !!:       !!:  !!!  !!:  !!:  !!!    !!:    
:!:       :!:  !:!  :!:       :!:       :!:  !:!     :!:       :!:  !:!  :!:  :!:  !:!    :!:    
 ::: :::  ::   :::   :: ::::   ::: :::   ::  :::      ::       ::::: ::   ::   ::   ::     ::    
 :: :: :   :   : :  : :: ::    :: :: :   :   :::      :         : :  :   :    ::    :      :   ''')
       
print("\n")
print ("Reputation Check for files, URLs & IP Adresses")
print ("Version 1.0 - Written by Michael Braun")
print("\n")
                 
            
#Main Functionality - Gather info and send to authentication

client_key = input("Enter your API Key: ")

token = auth_token(url,client_key)
token = token.decode('utf-8')


#Menu Options
selection=True
while selection:
    print ("Select option: \n")
    print("""
    1. Check a URL
    2. Check an IP Address
    3. Check a file (MD5 Hash)
    4. Exit/Quit
    """)
    selection=input("Select a task number: ")
    if selection=="1":
        res_type = "url"
        resource = input("Enter URL: ")

        post(token, client_key, resource, res_type)
    
    elif selection=="2":
            res_type = "ip"
            resource = input("Enter IP address: ")

            post(token, client_key, resource, res_type)
    elif selection=="3":
            res_type = "file"
            resource = input("Enter file MD5 Hash: ")

            post(token, client_key, resource, res_type)     
    elif selection=="4":
        print("\nGoodbye")
        sys.exit() 
        selection = None
    else:
        print("\n Not Valid Choice. Try again.")

