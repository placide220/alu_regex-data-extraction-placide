import re

def validate_phone_number(phone):
    """Validates phone numbers (various formats)."""
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.fullmatch(pattern, phone))

phones = ["(123) 456-7890", "123-456-7890", "123.456.7890", "000-000-"]

def phone_status(phone):
    return (phone, "Valid" if validate_phone_number(phone) else "Invalid")

results = list(map(phone_status, phones))

print("Phone Number Validation Summary:")
for phone, status in results:
    print(f"{phone}: {status}")