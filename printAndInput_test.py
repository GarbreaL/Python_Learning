import random
print("---begin---")
secret=random.randrange(10)
temp=input("输入一个数字:")
count=0
ismatching=False
while int(temp) !=secret:
    if int(temp)==secret:
        ismatching=True
    else:    
        if int(temp)>secret:
            temp=input("大了，再输入一个数字:")
        else:  
            temp=input("小了，再输入一个数字:")        
    count=count+1
    if count>2 and ismatching==False:
        print("3次机会已用完")
        break
if count==0 and ismatching==True:
    print("一次猜中，答案就是："+str(temp))
else:
    print("猜中，答案就是："+str(temp))            
print("---end---")    
