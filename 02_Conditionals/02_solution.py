age = int(input("Enter the age : "))
day = input("Enter day : ")
price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2
else:
    price = 12

print("Ticket price for you is $", price)