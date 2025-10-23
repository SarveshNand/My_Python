lister = [1, 2, 3, 4, 5, 6, 6 ,7 , 8, 9, 0]

lister = list(set(lister))
if len(lister) < 2:
    print(f"Not enough elements in {lister}")
else:
    lister.sort(reverse=True)
    print(f"The second largest number in the list is -> {lister[1]}")