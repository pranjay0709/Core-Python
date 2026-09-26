list = [92, 3, 56, 78, 53, 2, 9, 6]
print(max(list))
list.sort()
print(list)


leftover = list
leftover.remove(max(leftover))
print(max(leftover))
print(list)


l1 = [2, 4, 6, 4, 1, 8, 3, 0]
i = 0
while i < len(l1) - 1:
    if l1[i] > l1[i + 1]:
        l1[i], l1[i + 1] = l1[i + 1], l1[i]
        i = 0
    else:
        i += 1
print(l1)


