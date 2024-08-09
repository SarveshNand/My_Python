distance = int(input("Enter your Distance in Kms: "))

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
elif distance > 15:
    transport = "Car"

print("AI recommends you the Transport of: ",transport)