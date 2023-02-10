from twilio.rest import Client
sid='SID_DAALO_APNI'
auth='PASSWORD_DAALDO'
client=Client(sid, auth)
message=client.messages.create(to='whatsapp:+APNA_NUMBER_DAALO', from_ ='whatsapp:+14155238886',body='Hi, this is the test message')