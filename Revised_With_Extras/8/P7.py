def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
    return

table = int(input("Enter a number: "))
print(multiply(table))