from twilio.rest import Client
def message(number,message):
    sid='ACe30a0cc15a4ecb75e59013d1ab25211f'
    authToken='e7730d793b1d95a66010fdf6eb444917'
    client=Client(sid,authToken)
    
    message=client.messages.create(to='whatsapp:'+number,
                from_='whatsapp:+14155238886',body=message)