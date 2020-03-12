import twilio
from twilio.rest import Client
import random
otp = random.randint(1000,9999)
print(otp)

#  Your new Phone Number is +13342342628

account_sid = 'AC1dc069b1f8ad4eb5541d16f6da57cd25'
auth_token = '46723e46b07aa4a73989f923c43d377c'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='Your OTP is -'+str(otp),
         from_='+13342342628',
         to='+918619620054'
        )

print(message.sid)