a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
d = int(input("Enter number: "))
if (a>b and a>c and a>d):
    print("Greatest number is: ", a)
elif (b>a and b>c and b>d):
    print("Greatest number is: ", b)
elif (c>b and c>a and c>d):
    print("Greatest number is: ", c)
elif (d>b and d>a and d>c):
    print("Greatest number is: ", d)
else:
    print("There are equal number of values present in the variables given")