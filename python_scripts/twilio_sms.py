# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC6db14b33d7d3d8d779adcae7cedf8675'
auth_token = 'e69fc0f98c84e265beb300a30ba41ccc'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Check this out! Did it work? (from Cory)",
                     from_='+12056199447',
                     to='+19143124643'
                 )

print(message.sid)