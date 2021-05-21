# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACdcdbf4b392bf649d0d5e61ebbde7bbe1'
    auth_token = '8e4a86068cfe26751c210f98ccde105a'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+14843696040',
                        to='+18097772662'
                    )

    print(message.sid)

