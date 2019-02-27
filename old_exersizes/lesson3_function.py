#定义函数
def MyFirstFunction():
    """
    函数说明是在这里
    可以写很多行
    """  
    print("This is MyFirstFunction")

#调用函数
MyFirstFunction()    
#函数说明查看
print("函数说明查看方式：MyFirstFunction.__doc__")
print(MyFirstFunction.__doc__)


#多参数
def MySecondFunction(name,age):
    print(name +'年龄是:'+age)
#参数可以通过形参名配合实参，不需要考虑顺序
MySecondFunction(age='18',name='校长')

#参数的默认值
def MyThirdFunction(name='校长',age='20'):
    print(name +'年龄是:'+age)

#没有传递参数的，会使用默认参数
MyThirdFunction(age="50")    
