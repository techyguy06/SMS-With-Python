# Send SMS with Python Using TWILIO
from twilio.rest import Client

account_sid = '<Your SID>'
auth_token = '<Auth Token>'
client = Client(account_sid, auth_token)

message = client.messages.create(
				from_='<from_number>',
				body='<Message to send>',
				to='<to_number>'
			)

print(message.sid)