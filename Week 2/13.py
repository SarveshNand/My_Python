def create_set(n1, n2):
    val1 = n1.intersection(n2)
    val2 = n1.union(n2)
    val3 = n1.difference(n2)
    return f"Union: {val2}, Intersection: {val1} and Difference: {val3}"

set1 = {3, 4}
set2 = {2, 4}
print(create_set(set1, set2))