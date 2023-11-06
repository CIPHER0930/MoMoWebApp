import requests
import json
import base64

BASE_URL = "https://momodeveloper.mtn.cm"
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

# Get the sender's phone number
sender_phone_number = input("Enter the sender's phone number: ")

# Get the sender's phone number's pin code
sender_phone_number_pin_code = input("Enter the sender's phone number's pin code: ")

# Get the receiver's phone number
receiver_phone_number = input("Enter the receiver's phone number: ")

# Get the amount to transfer
amount = input("Enter the amount to transfer: ")

headers = {
    "Authorization": f"Basic {base64.b64encode(f'{API_KEY}:{API_SECRET}'.encode('utf-8')).decode('utf-8')}",
}

json = {
    "senderPhoneNumber": sender_phone_number,
    "receiverPhoneNumber": receiver_phone_number,
    "amount": amount,
    "currency": "XAF",
}

# Check if the pin code is correct
if pin_code != sender_phone_number_pin_code:
    print("Pin code incorrect!")
    exit(1)

try:
    # Send the transfer request to MTN MoMo
    transfer_response = requests.post(
        f"{BASE_URL}/transfer",
        headers=headers,
        json=json,
    )

    # Check the response status code
    if transfer_response.status_code == 200:
        # Transfer successful!
        print("Transfer successful!")

        # Display the transfer ID
        print(f"Transfer ID: {transfer_response.json()['transferId']}")
    else:
        # Transfer failed!
        print("Transfer failed!")
except Exception as e:
    # Handle any errors that may occur
    print(f"Error: {e}")
