def remove_duplicates(l):
    d =[]
    for i in l:
        if i not in d:
            d.append(i)
    return d

c=['Angola', 'Maldives', 'Angola',  'India', 'United States', 'India']
a=  set(c)
print(a)

c=['Angola', 'Maldives', 'India']
a=  remove_duplicates(c)
print(a)

squares = set()

maxs = int(2000**(1/2.))
for i in range(maxs,0,-1):
    squares.add(i**2)
print(squares)

for i in range(10,0,-1):
    print(i)

print(range(10))