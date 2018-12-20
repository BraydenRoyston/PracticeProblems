# This program takes an input of a list, and then take an input of a number.
# The program then outputs any numbers in the initial list that are less than the second input.


list1 = [int(x) for x in input("Enter the list, and be sure to separate different arguments by a space:").split()]
listLessThan = []
y = int(input("Enter the integer you want the results to be less than:"))

for x in list1:
    if x < y:
        listLessThan += [x]
    else:
        continue

print(listLessThan)
