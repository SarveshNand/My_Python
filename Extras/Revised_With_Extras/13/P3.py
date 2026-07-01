def divisible(n):
    if(n%5==0):
        return True
    return False

a = [1, 2, 324, 4546745, 3243, 34235445, 45, 676]

f = list(filter(divisible, a))
print(f)