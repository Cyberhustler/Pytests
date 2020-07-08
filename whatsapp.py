import os
from twilio.rest import Client

account_sid = os.getenv("DATABASE_Ua")
auth_token = os.getenv("DATABASE_PASSWORD")
client = Client(account_sid, auth_token)


def send_love():
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Good Morning you biscuit i hope you slept'
                                    'well im so sorry gonna pass out soon',
                              to='whatsapp:+yournuber'
                          )

    print(message.sid)
