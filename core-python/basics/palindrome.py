number=151
num =number
reversed_number = 0
while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number*10)+last_digit
    number = number // 10
if num == reversed_number:
    print(reversed_number,"This number is palindrome")
else:
    print("not a palindrome")