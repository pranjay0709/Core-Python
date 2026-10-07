print('Start')

a = 10
b = 0
print('mid')
try:
    c = a / b
    print('Divison', c)
except ZeroDivisionError as e:
    print('exception', e)
print('End')
