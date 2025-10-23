fib = int(input("Enter how many Fibonacci numbers you want: "))
a = 0
b = 1
print("Fibonacci Sequence: ")
for i in range(fib):
    print(a, end=' ')
    a, b = b, a + b
    