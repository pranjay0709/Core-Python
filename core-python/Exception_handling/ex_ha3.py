print('Start')

a = 10
b = 2
print('mid')
try:
    c = a / b
    print('Divison', c)
except ZeroDivisionError as e:
    print('exception', e)
else:
    print('Else works after try executes')
print('End')
