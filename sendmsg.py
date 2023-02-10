from twilio.rest import Client
sid='ACe30a0cc15a4ecb75e59013d1ab25211f'
auth='dcc216cc5b4b42f09449f3816697f7c0'
client=Client(sid, auth)
message=client.messages.create(to='whatsapp:+919310329696', from_ ='whatsapp:+14155238886',body='Hi, this is the test message')