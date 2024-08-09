from functools import reduce
l = [1, 2, 324, 4545, 5445, 45, 676]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))