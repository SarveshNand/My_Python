ev_od = int(input("Enter a Number: "))
if ev_od % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


for num in range(5, 101, 5):
    print(num)


num = int(input("Enter a positive number: "))
if num < 0:
    print("Enter a Positive Number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")