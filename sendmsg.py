from twilio.rest import Client
def message(number,message):
    sid='PUT_SiD_no.'
    authToken='put_password'
    client=Client(sid,authToken)
    
    message=client.messages.create(to='whatsapp:'+number,
                from_='whatsapp:+14155238886',body=message)
