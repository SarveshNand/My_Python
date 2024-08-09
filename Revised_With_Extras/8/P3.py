def sum(n):
    if (n == 1):
        return 1
    return sum(n-1) + n

number = int(input("Enter a number: "))
print(sum(number))