def even_gen(n):
    for num in range(0, n + 1, 2):
        yield num

N = int(input("Enter a number: "))
print(f"Even numbers up to {N}: ")

for even in even_gen(N):
    print(even)