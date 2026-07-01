def sq_dict():
    square_dict = {}
    for i in range(1, 11):
        square_dict[i] = i * i
    return square_dict

result = sq_dict()
print("Dictionary of Squares: ", result)