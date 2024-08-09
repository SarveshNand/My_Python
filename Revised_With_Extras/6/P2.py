Subject1 = int(input("Enter marks: "))
Subject2 = int(input("Enter marks: "))
Subject3 = int(input("Enter marks: "))

total_percentage = ((Subject1+Subject2+Subject3 / 3) >= 40)

if((Subject1 > 33 and Subject2 > 33 and Subject3 > 33) and total_percentage):
    print("The Student has been passed.")
else:
    print("The Student has been failed.")