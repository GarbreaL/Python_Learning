#--------------------------
#1、输入输出函数
#2、逻辑判断
#3、循环及跳出循环
#4、引入系统模块
#--------------------------
import random

loopCount = 0
defaultValue = random.randrange(5,10)
userInput = input(r"请输入一个数字[5-10]，看看是否与系统随机数一样：")
if defaultValue ==int(userInput):
    print("太厉害了，一下就猜中了")
else:    
    while defaultValue!=int(userInput):
        if defaultValue > int(userInput):
            userInput = input(r"数字小了,再猜一下：")
        else:
            userInput=input(r"数字大了，再猜一下：") 
        loopCount = loopCount + 1
        if loopCount > 3:
            print("三次没有猜中，逊毙了")
            break
        else:
            continue
    if loopCount<=3 and defaultValue ==int(userInput):
        print("猜中了，系统随机数是：" + str(defaultValue))
        