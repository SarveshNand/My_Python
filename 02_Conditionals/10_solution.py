leap_year = int(input("Enter year:"))

if(leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
    print(leap_year, "is a Leap Year")
else:
    print(leap_year, "is a Non-Leap Year")