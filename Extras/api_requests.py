import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

# if response.status_code == 200:
#     posts = response.json()
#     for post in posts:
#         title = post.get('title')
#         print(title)
# else:
#     print(f"Failed to fetch posts: HTTP {response.status_code}")



requester = {"user_name": "sarvesh",
             "password": "testing"}
requesting = requests.post(url, json=requester)
print(requesting.text)