import re

def extract_hashtags(tweet):
    hashtags = re.findall(r'#\w+', tweet)
    return hashtags

tweet = "Loving the weather today! #sunshine #happy #weekendVibes"
hashtags = extract_hashtags(tweet)

print("Hashtags found: ", hashtags)