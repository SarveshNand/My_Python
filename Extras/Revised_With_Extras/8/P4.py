def pattern(n):
    if (n==0):
        return 0
    print("*" * n)
    pattern(n-1)

star = int(input("Enter a number: "))
print(pattern(star))