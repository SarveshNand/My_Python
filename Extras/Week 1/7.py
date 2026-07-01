n = int(input("Enter a positive number: "))
if n < 0:
    print("Enter a positive number")
if n == 0:
    print("The Factorial of 0 is 1")
if n > 0:
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}")