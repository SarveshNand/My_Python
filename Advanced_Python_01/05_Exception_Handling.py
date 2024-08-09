try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyyyy")
    print(v)
except Exception as e:
    print(e)
except TypeError as t:
    print(t)
except ZeroDivisionError as z:
    print(z)

print("Thank You")