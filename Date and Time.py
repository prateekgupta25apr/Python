import datetime

d = datetime.datetime.now()
e = d - (d - datetime.timedelta(hours=48))
if e.days == 1:
    print("if")
else:
    print("else")
