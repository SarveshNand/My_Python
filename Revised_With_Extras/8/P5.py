def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"{inch_to_cms(n)} in centimeters")