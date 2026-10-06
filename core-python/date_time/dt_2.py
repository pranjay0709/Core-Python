import datetime
today=datetime.date.today()
print(today)

future = today+datetime.timedelta(days=14)
past = today - datetime.timedelta(days=14)
print("Future date :", future)
print("Past date :",past)
