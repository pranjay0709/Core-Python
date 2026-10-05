def arm_no(num):
    rem = 0
    n = num
    sum = 0
    while (n > 0):
        r = n % 10
        sum = sum + r * r * r
        n = n // 10
    if num == sum:
        print(num, " Is an Armstrong number")
    else:
        print(num, " Is not an Armstrong number")

arm_no(153 )