class Lg_ex(Exception):
    def __init__(self,msg):
        super().__init__(msg)

login_id=input("Enter Id:")
password=input("Enter Password:adm")

try:
    if login_id=='admin' and password=='admin':
        print('Valid user')
    else:
        raise Lg_ex('Invalid user')
except Lg_ex as e:
    print('Exception:', e)

