#键值对
dict1={1:"one",2:"tow",3:"three"}


for eachkey in dict1.keys():
    print(eachkey)    
#get,pop,popitme
for eachitem in dict1.items():
    print(eachitem)
#update
dict1.update({4:"four"})
print(dict1)
#pop之后，值被清除了   
print(dict1.pop(2))
dict1.update({3:'三'})
print(dict1)