time_min_1 = 30

hours_1 = time_min_1 // 60
minutes_1 = time_min_1 % 60

time_format = "{} hours {} minutes".format(hours_1,minutes_1)

print(time_format)