from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

client.messages.create(
    to="+10000000000",
    from_="+10000000000",
    body="Hey this is a text message"
)
