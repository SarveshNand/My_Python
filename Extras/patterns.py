# 1
# rows = int(input("Rows = "))
# cols = int(input("Columns = "))
# for i in range(rows):
#     print("*" * cols, end="")
#     print()


# 2
# rows = int(input("Rows = "))
# for i in range(1, rows + 1):
#     print("*" * i)


# 3
# rows = int(input("Rows = "))
# for i in range(1, rows+1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()


# 4
# rows = int(input("Rows = "))
# for i in range(1, rows+1):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()


# 5
# rows = int(input("Rows = "))
# for i in range(rows, 0, -1):
#     print("*" * i)


# 6
# rows = int(input("Rows = "))
# for i in range(rows+1, 0, -1):
#     for j in range(1, i):
#         print(j, end="")
#     print()


# 7
# rows = int(input("Rows = "))
# for i in range(1, rows + 1):
#     spaces = rows - i
#     stars = 2 * i - 1
#     print(' ' * spaces + '*' * stars)


# 8
# rows = int(input("Rows = "))
# for i in range(rows, 0, -1):
#     spaces = rows - i
#     stars = 2 * i - 1
#     print(' ' * spaces + '*' * stars)


# 9
# rows = int(input("Rows = "))
# for i in range(1, rows + 1):
#     spaces = rows - i
#     stars = 2 * i - 1
#     print(' ' * spaces + '*' * stars)
# for i in range(rows, 0, -1):
#     spaces = rows - i
#     stars = 2 * i - 1
#     print(' ' * spaces + '*' * stars)


# 10
# rows = int(input("Rows = "))
# for i in range(1, rows + 1):
#     print("*" * i)
# for i in range(rows - 1, 0, -1):
#     print("*" * i)


# 11
# rows = int(input("Rows = "))
# for i in range(1, rows + 1):
#     for j in range(i):
#         print((j + 1) % 2, end=' ')
#     print()


# 12
# rows = int(input("Rows = "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     if i < rows:
#         print(' ' * (2 * (rows - i)), end='')
#     else:
#         print(str(i) * (2 * (rows - i)), end='')
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()


# 13
rows = int(input("Rows = "))
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()