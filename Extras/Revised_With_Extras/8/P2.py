def f_to_c():
    return 5 * (f - 32) / 9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f" {round(c, 2)} in Celsius")