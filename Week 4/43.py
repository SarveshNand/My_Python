import re

def is_valid_url(url):
    # Regex pattern to validate most URLs (http, https, ftp)
    pattern = re.compile(
        r'^(https?|ftp)://'                # protocol
        r'(\w+(\-\w+)*\.)+'                # domain name segments (e.g. www., subdomain.)
        r'[a-zA-Z]{2,}'                   # top-level domain
        r'(:\d+)?'                       # optional port
        r'(\/[^\s]*)?$',                 # optional path
        re.IGNORECASE
    )
    return re.match(pattern, url) is not None

test_urls = [
    "https://www.example.com",
    "ftp://ftp.example.com/resource.txt",
    "http://localhost",
    "invalid_url.com",
    "https://example"
]

for url in test_urls:
    print(f"{url} -> {'Valid' if is_valid_url(url) else 'Invalid'}")