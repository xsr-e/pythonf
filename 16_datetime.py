from datetime import date, datetime, time, tzinfo

d_today = date.today()
dt_now = datetime.now()

date_str =d_today.strftime("%d.%m.%Y")
date_iso = d_today.isoformat()


print((d_today,dt_now,date_str,date_iso))

