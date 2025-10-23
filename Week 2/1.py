def is_even(n):
    if n % 2 == 0:
        return "It is even"
    else:
        return "It is odd"
    
n = int(input("Enter a number: "))
print(is_even(n))