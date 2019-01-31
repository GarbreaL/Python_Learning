def displayInventory(inventory):
	if isinstance(inventory,dict):
		totalcount=0
		itemcount={}
		for k,v in inventory.items():
			itemcount.setdefault(k,0)
			itemcount[k]=itemcount[k]+int(v)
			totalcount=totalcount+int(v)
		print('Inventory:')
		for k,v in itemcount.items():
			print(str(v)+'--'+k)
		print('The totalcount of inventory is :'+str(totalcount))
	else:
		print('please input dict as function args')

#把列表中的物品数量添加到字典中，有的累加，没有的新增为1.
def addToInventory(inventory,addedItems):
	for i in range(len(addedItems)):
		#用get()方法可以设置默认值
		inventory[addedItems[i]]=int(inventory.get(addedItems[i],0))+1

inv={'gold coin':2,'rope':2,'banana':2}
dragonLoot=['gold coin','dagger','gold coin','ruby','gold coin','ruby','apple']
addToInventory(inv,dragonLoot)
displayInventory(inv)
