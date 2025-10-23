with open("name.txt", "w") as f:
    writer = f.write("Sarvesh Nand")
    print(writer)

with open("name.txt", "r") as f:
    reader = f.read()
    print(reader)