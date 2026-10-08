a=int(input("Enter a number:"))

try:
    if a<=10:
        print("you number is valid", a)
    else:
        raise Exception('Invalid number')
except Exception as e:
    print('exception', e)