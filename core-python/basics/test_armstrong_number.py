number = 152
rem = 0
sum = 0
n = number

while n > 0:
    rem = n % 10
    sum = sum + (rem * rem * rem)
    n = n // 10

if number == sum:
    print('armstrong number')
else:
    print('not armstrong number')
