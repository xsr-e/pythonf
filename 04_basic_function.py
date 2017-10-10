def format_minutes(minutes):
    '''gets formatted time from minutes'''
    days = minutes // (60*24)
    hours = (minutes // 60) % 24 
    minutes = minutes % 60
    formatted = "{0} days, {1} hours, {2} minutes".format(days,hours,minutes)
    return formatted
def print_f(minutes):
    '''prints formatted time from minutes'''
    print (format_minutes(minutes))

print_f(30)
print_f(60)
print_f(90)
print_f(1515)
print_f(1440)