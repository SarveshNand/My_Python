# Let us say your expense for every month are listed below,
#    January - 2200
#    February - 2350
#    March - 2600
#    April - 2130
#    May - 2190
# Create a list to store these monthly expenses and using that find out,


exp = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("1) Dollars spent extra compared to January: ", exp[1]-exp[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print("2) Total expense in first quarter (first three months) of the year: ", exp[0]+exp[1]+exp[2])

# 3. Find out if you spent exactly 2000 dollars in any month.
print("3) Did I spent 2000$ in any month? ", 2000 in exp)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("4) June month expense added: ", exp)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
exp[3] = exp[3] - 200
print("5) Corrected List after Refund: ",exp)





# You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

# Using this find out,

# 1. Length of the list
print("6) Length: ", len(heros))

# 2. Add 'black panther' at the end of this list
heros.append("black Panther")
print("7) Adding Black Panther: ", heros)

# 3. You realize that you need to add 'black panther' after 'hulk',    so remove it from the list first and then add it after 'hulk'
heros.remove("black Panther")
heros.insert(3, "black Panther")
print("8) Correcting the list: ", heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ["doctor strange"]
print("9) Updated List: ", heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print("10) Sorted List: ", sorted(heros))




# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

user_input = int(input("* Give a number here so that I can find odd numbers: "))
odd_numbers = [i for i in range(1, user_input + 1) if i % 2 != 0]
print("* Odd numbers:", odd_numbers)