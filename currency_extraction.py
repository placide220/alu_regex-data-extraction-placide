import re

def validate_usd_currency(amount):
    """Validates US dollar currency format like $19.99 or $1,234.56."""
    pattern = r'^\$\d{1,3}(?:,\d{3})*(?:\.\d{2,})?$|^\$\d+(?:\.\d{2})?$'
    return bool(re.fullmatch(pattern, amount))

currencies = [
    "$19.99",
    "$1,234.56",
    "$100",
    "$12,345",
    "$12,345.67",
    "$123456.78",
    "19.99",
    "$1,234.567",
    "$1,23.45"
]

for amount in currencies:
    print(f"{amount}: {'Valid' if validate_usd_currency(amount) else 'Invalid'}")