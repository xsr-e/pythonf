
# list
list_int = [1,2,2,2,3]
print (list_int)


#set
set_int = set(list_int) #order is not guaranteed
print (set_int)

#dictionary
dict_int = {1:'A',2:'B'}
print(dict_int)
print(dict_int[2])

n=dict_int.get(100)
print(n)

# dict_int[100] # KeyError 100

#dictionary from list
dict_from_list = dict.fromkeys(range(4),range(5))
print dict_from_list

#dictionary from set
dict_from_set = dict.fromkeys(set_int,0)
print dict_from_set


codes = {}
for n in range(65,123):
    codes[n]=chr(n)

print codes
