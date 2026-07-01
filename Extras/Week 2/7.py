def convert_lis_tup(n):
    num1 = tuple(n)
    num2 = list(num1)
    return f"Tuple : {num1}\nList : {num2}"

lister = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(convert_lis_tup(lister))