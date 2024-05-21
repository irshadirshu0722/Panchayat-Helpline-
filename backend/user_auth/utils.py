import random
from twilio.rest import Client
from django.conf import settings
def send_otp(phone_number,otp):
  client  = Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)
  response = client.messages.create(
    body=f"Your otp is {otp}",
    from_=settings.TWILIO_PHONE_NUMBER,
    to=phone_number,
  )
  print(response.error_message)
  return otp
def generate_otp():
    return random.randint(100000, 999999)