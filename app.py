from datetime import date, datetime, time, tzinfo

d = date.today()
dt = datetime.now()
#t = time.isoformat(d.time)
e =d.strftime("%Y-%m-%d")


s = (d,e,d.isoformat(),dt)
print(s)