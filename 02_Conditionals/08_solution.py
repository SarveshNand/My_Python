Pet = input("Enter your pet specie: ")
age = int(input("Age of your pet: "))

if age < 2:
    print("Puppy Food to your", Pet)
elif age <= 5:
    print("Milk to your",Pet)
elif age > 5:
    print("Nutrients to your",Pet)