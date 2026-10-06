import datetime
from time import strftime

today=datetime.datetime.today()
format=strftime("%d-%m-%y")
print("Today's Date:   ", format)