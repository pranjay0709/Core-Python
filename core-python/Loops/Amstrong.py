number = 153
num = number
r = 0
sum = 0

while (num > 0):
    r = num % 10
    sum = sum + r * r * r
    num = num // 10

if number == sum:
    print(" this  number is Amstrong No", sum)
else:

    print(" this is number is not Amstrong No", sum)
