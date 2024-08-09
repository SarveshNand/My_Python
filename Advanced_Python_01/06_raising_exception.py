a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey Our Program is not meant to be divided by Zero")
else:
    print(f"The division a/b is {a/b}")