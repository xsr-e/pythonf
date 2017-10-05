time_min_1 = 30

hours_1 = time_min_1 // 60
minutes_1 = time_min_1 % 60

time_format = "{} hours {} minutes".format(hours_1,minutes_1)

print(time_format)

weight,height = 100, 1.7
bmi = weight/height**2
bmi_f = "%.2f" % bmi
msg = "weight {}kg, height {}m, bmi:{}".format(weight,height,bmi_f)
print(msg)