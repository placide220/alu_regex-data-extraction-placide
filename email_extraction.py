import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def validate_email(email):
    """Validates an email address."""
    return bool(EMAIL_PATTERN.fullmatch(email))

# Test Cases
emails = [
    "user@example.com",
    "firstname.lastname@company.co.uk",
    "wrong@format",
    "test@com",
]

results = [f"{email}: {'Valid' if validate_email(email) else 'Invalid'}" for email in emails]
print('\n'.join(results))