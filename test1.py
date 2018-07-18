print("hello word!")
print("---------------------")
n=123
print(n) #这样可以写注释
f=456.789
print(f)
s1=r"hello python"
print(s1)
s2=r'''hello
 vs code ''' #字符串里面的回车也会被打印出来
print(s2)
print("---------------------")
print("input 接收键盘输入：")
str_input=input("输入数字1：")
num1=int(str_input)
str_input=input("输入数字2：")
num2=int(str_input)
num3=num2+num1
print(str(num1)+"+"+str(num2)+"="+str(num3))
str_input="Hello world"
for i in str_input:
    print(i,end='\n') #1个字符打印一行
