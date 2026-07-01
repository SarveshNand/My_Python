def access_tuple(n):
    my_tuple = ("apple", "banana", "cherry", "date")

    if 0 <= n < len(my_tuple):
        return my_tuple[n]
    else:
        return "Index out of range"
    
print(access_tuple(1))
print(access_tuple(5))