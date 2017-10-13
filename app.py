f = open('tmp.py', 'r')
data = f.read()
print data
f.close()

with open('/Users/usr/git/pythonf/log_data.txt','w') as log:
    for i in range(10):
        log.write("Log line no:{}\r".format(i))


