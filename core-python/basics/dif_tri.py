num = 5
for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

number = 5
for i in range(number):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

for i in range(1, num + 1):
    print(" " * (num - i) + '*' * i)
print()

for i in range(1,num+1):
    print(" " * (num-i) + '* '*i)
print()

for i in range(1,num+1):
    print(" " * (num-i) + ' *'*i)
for i in range(num,0,-1):
    print(" " * (num-i) + ' *'*i)
print()


