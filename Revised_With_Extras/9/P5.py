words = ["Donkey", "bad", "ganda"]

with open("file1.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file1.txt", "w") as f:
    f.write(content)