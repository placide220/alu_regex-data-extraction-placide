import re

def validate_url(url):
    """Validates URLs (http, https, subdomains, and paths)."""
    pattern = r'^(https?://)?(www\.)?[\w.-]+\.[a-z]{2,6}(/\S*)?$'
    return bool(re.fullmatch(pattern, url))


urls = ["https://www.example.com", "http://subdomain.example.org/page", "ftp://invalid.com"]
for url in urls:
    print(f"{url}: {' Valid' if validate_url(url) else 'Invalid'}")



