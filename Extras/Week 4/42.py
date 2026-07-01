import re

def is_valid_email(email):
    # Basic regex pattern for validating an email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

emails = ["test.email@example.com", "invalid-email@", "user@domain", "user@domain.co.uk"]

for email in emails:
    if is_valid_email(email):
        print(f"'{email}' is a valid email.")
    else:
        print(f"'{email}' is NOT a valid email.")