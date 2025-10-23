num = int(input("Enter a number: "))
str_num = str(num)
if str_num == str_num[::-1]:
    print("The number is palindrome")
else:
    print("The number is not palindrome")