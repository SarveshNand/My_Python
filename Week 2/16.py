def check_palin(string):
    if string == string[::-1]:
        return f"{string} is palindrome"
    else:
        return f"{string} is not palindrome"

string = input("Enter something: ")
print(check_palin(string))