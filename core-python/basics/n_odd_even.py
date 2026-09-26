number = 10
odd_sum = 0
cur_odd = 1
for i in range(number):
    odd_sum += cur_odd
    cur_odd = +2
print(odd_sum,"odd_sum")
average_odd= odd_sum/number
print(average_odd,"average_odd")

even_sum = 0
cur_even = 2
for i in range(number):
    even_sum += cur_even
    cur_even = +2
print(even_sum,"even_sum")
average_even= even_sum/number
print(average_even,'average_even')