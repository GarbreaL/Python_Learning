#数组
member=["John","Tom","Rose"]
mix=["John",30,3.14,["Monther","Father"],[]]

#数组增加的3种方法append，extend，insert
member.append("GoldenWater")
print(member)
member.extend(["张三","李四"])
print(member)
member.insert(1,"中英文")
print(len(member))
member.reverse() #翻转
print(member)

#数组的删除
member.remove("John") #remove的必须是字符全匹配
print(member)
del member[1]
print(member)
str_pop=member.pop() #pop,取index最大的
print("pop="+str_pop)
print(member) 
str_pop=member.pop(2)
print("pop="+str_pop)
print(member) 

#数组的分片
member=["John","Tom","Rose","GoldenWater","Younger","Bigger"]
member2=member[1:2] #Tom
print(member2)
member2=member[3:]
print(member2)
#member2和member指向同一个值，其中一个改变，另一个也随着改变
member2=member  
print(member2)
member.append("Smaller")
print(member2)
#member3是member的拷贝，其中一个改变，另一个不会随着改变
member.remove("Smaller")
member3=member[:]  
print(member3)
member.append("Shotter")
print(member3)