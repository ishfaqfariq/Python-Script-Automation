from twilio.rest import Client

# Replace these values with your actual Twilio credentials
account_sid = "AC89401013585a5e3221bffc9dfd7fff7b"
auth_token = "56288cc5dc54b226fdf355c9db3e1748"

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Retrieve the list of incoming phone numbers
try:
    incoming_phone_numbers = client.incoming_phone_numbers.list()
    
    # Assuming you have at least one incoming phone number
    if incoming_phone_numbers:
        first_incoming_number = incoming_phone_numbers[0]
        from_number = first_incoming_number.phone_number
        print(f"Your Twilio phone number: {from_number}")
    else:
        print("No incoming phone numbers found in your account.")
except Exception as e:
    print(f"Error retrieving incoming phone numbers: {str(e)}")
