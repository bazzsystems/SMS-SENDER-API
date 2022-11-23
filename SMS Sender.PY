from twilio.rest import Client 
 
account_sid = '#ACCOUNTSID' 
auth_token = '#AUTH KEY' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='#api ID', 
                              body='TEXT HERE',      
                              to='+972123456789' 
                          ) 
 
print(message.sid)