import requests
import json
import base64
from momoapi import getBalance

BASE_URL = "https://momodeveloper.mtn.cm"
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

# Define a function to validate the API key and secret
def validate_api_key_secret(api_key, api_secret):
 if not api_key or not api_secret:
  raise ValueError("Invalid API key or secret")

# Define a function to check MTN MoMo account balances
def check_balance(phone_number):
 # Validate the API key and secret
 validate_api_key_secret(API_KEY, API_SECRET)

 # Generate the authorization header
 headers = {
  "Authorization": f"Basic {base64.b64encode(f'{API_KEY}:{API_SECRET}'.encode('utf-8')).decode('utf-8')}",
 }

 # Make the request to the MTN MoMo API
 try:
  balance_response = requests.get(
    f"{BASE_URL}/getBalance?phoneNumber={phone_number}",
    headers=headers,
  )
 except Exception as e:
  raise Exception("Failed to check account balance: " + str(e))

 # Check the response status code
 if balance_response.status_code == 200:
  # Success!
  return balance_response.json()["balance"]
 else:
  # Error!
  raise Exception("Failed to check account balance: " + str(balance_response.status_code))

# Get the sender's phone number
sender_phone_number = input("Enter the sender's phone number: ")

# Validate the sender's phone number
validate_phone_number(sender_phone_number)

# Check the sender's account balance
sender_balance = check_balance(sender_phone_number)

# Print the sender's account balance
print(f"The sender's phone number is {sender_phone_number}.")
print(f"The sender's account balance is {sender_balance} XAF.")
