class Robot:
    #----属性--双下划线表示私有---
    __id=""
    #----方法--------
    #方法中需要有self
    def __init__(self,id):#构造函数（参数）
        self.__id=id
    def getID(self):
        return self.__id
    def GetOrder(self):
        print('接收指令---')
    def ExcuteOrder(self):
        print('执行指令---')
    def Charge(self):
        print('充能---')

r=Robot('xiaoc')
print('Robot id is %s' % r.getID())


# --issubclass 一个类是否是另一个类的子类
# --isinstance 一个对象是否是一个类的实例
