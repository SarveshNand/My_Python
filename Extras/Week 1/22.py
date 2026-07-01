num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp //= 10

if sum == num:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")