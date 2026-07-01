num = int(input("Enter the number: "))
count_of_digits = 0
num = abs(num)
if num == 0:
    count_of_digits = 1
else:
    while num > 0:
        num = num // 10
        count_of_digits += 1
print(f"Count of Digits : {count_of_digits}")