#错误捕捉了，发生错误代码行后的代码不会执行
'''
try:
    #i=1+'1'
    f=open("filenotexist.txt")
    print(f.read())
    i=1+'1'#这里发生错误，f不会执行close,需要在finally中关闭
    f.close()
except OSError as ex:
    print('文件不存在\n错误原因是：'+str(ex))
except TypeError as ex:
    print('类型出错了\n错误原因是：'+str(ex))
finally:
    f.close()   
'''
#使用with 关键字，可以完成整个文件操作
try:
    with open('test.txt') as open_file:
        print(open_file.read())
except OSError as ex:
    print("出错了\n错误原因是："+str(ex))    