import re

# Define the regular expression pattern
pattern = r'^\+998\(93\)-\d{3}-\d{2}-\d{2}$'

# Function to validate phone numbers
def validate_phone_number(phone_number):
    if re.fullmatch(pattern, phone_number):
        return True
    return False
