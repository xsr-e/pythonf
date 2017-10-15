f = open('tmp.py', 'r')

line = f.readline()
while line <> '':
    print line
    line = f.readline()
f.close()




with open('/Users/usr/git/pythonf/log_data.txt','w') as log:
    for i in range(10):
        tpl = (i,2**i)
        log.write("Log line no:{}\r".format(tpl))


