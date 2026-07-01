import re

def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

html_string = "<p>Hello, <b>world</b>! Welcome to <a href='#'>ChatGPT</a>.</p>"
cleaned = remove_html_tags(html_string)
print(cleaned)