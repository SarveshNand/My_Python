lister = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even_lister = 0

for i in lister:
    if i % 2 == 0:
        even_lister += i

print(f"Sum of even numbers: {even_lister}")