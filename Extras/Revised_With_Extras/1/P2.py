import os

# Specify the directory we want to list
directory_path = '/MinGW'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and director name
for item in contents:
    print(item)