import random

random_num = random.randint(1, 100)
count = 0
num = int(input("Enter a number: "))
while random_num != num:
    if random_num > num:
        print("You guessed low!")
    else:
        print("You guessed high!")
    num = int(input("Try Again: "))
    count += 1
print(f"Bingo you guessed right in {count} counts!!!")