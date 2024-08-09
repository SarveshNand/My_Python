marks = int(input("Enter your marks : "))

if marks >= 101:
    print("Please verify your Grade")
    exit()

if marks >= 90:
    print("You grade is A")
elif marks >= 80:
    print("Your grade is B")
elif marks >= 70:
    print("Your grade is C")
elif marks >= 60:
    print("Your grade is D")
else:
    print("Congrats! You got F; Now you are Officially Failed")