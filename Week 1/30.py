num = int(input("Enter a number: "))
print(f"Cube of numbers from 1 to {num}:")
for i in range(1, num + 1):
    cube = i ** 3
    print(f"{i}^3 = {cube}")