#元组 tuple 列表 list
"""
元组的特征是有英文的逗号,只有一个元素的元组必须以英文逗号作为结尾，才能被识别成一个有效的元组类型
元组与列表不一样，元组不能随意改变元组的值
但是元组可以通过拼接，生成一个新的元组,拼接的对象必须是元组
元组不支持remove
元组可以进行del操作
"""

array1=["JACK","TOM","ROSE","GOLDEN","WATER"]
print(str(type(array1)))
tuple1=(1,2,3,4,5,6,7)
print(str(type(tuple1)))
#把100拼接到元组的第2个元素后面
tuple1=tuple1[:2]+("100","200",300)+tuple1[2:]
print(tuple1)
for o in tuple1:
    print(type(o))


