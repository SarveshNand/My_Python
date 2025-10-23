import re

def find_emails(text):
    # Simple regex pattern to match most email addresses
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    return emails

sample_text = """
Hello John, please contact me at example.email@gmail.com or work-email@company.co.uk.
Also, you can reach out to admin@mysite.org for support.
"""

found_emails = find_emails(sample_text)
print("Email addresses found:", found_emails)