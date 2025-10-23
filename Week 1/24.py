a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operand = input("Enter in (+, -, *, /): ")

if operand == "+":
    print(a + b)
elif operand == "-":
    print(a - b)
elif operand == "/":
    print(a / b)
elif operand == "*":
    print(a * b)
else:
    print("Invalid operand")