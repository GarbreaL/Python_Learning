import sys
sys.setrecursionlimit(1000000)
def fibonacci(num1):
    if num1<=2:
        return 1
    else:
        return fibonacci(num1-1)+fibonacci(num1-2)
result=fibonacci(20)        
'''
递归效率比较低，数字改成30，系统计算明显变慢
'''
print("递归20次后斐波那契数是 %d" %(result))

'''用迭代方式实现'''
def fib2(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        return -1
    else:
       while(n-2)>0:
           n3=n2+n1
           n1=n2
           n2=n3
           n-=1
    return n3
result=fib2(20)                     
print("迭代20次后斐波那契数是 %d" %(result))            

