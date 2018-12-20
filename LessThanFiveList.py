list1 = [int(x) for x in input("Enter the list, and be sure to separate different arguments by a space:").split()]
list2 = []
y = int(input("Enter the integer you want the results to be less than:"))

for x in list1:
    if x < y:
        list2 += [x]
    else:
        continue

print(list2)
