def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Sarvesh", "Samira", "Rahul", "Aizen", "Death", "Peace"]

print(rem(l, "en"))