#打印字典key value item
def printDicKeys(birthday):
	print('---The keys of Dic as following:')
	for key in birthday.keys():
			print(key)

def printDicValues(birthday):
	print('---The values of Dic as following:')
	for value in birthday.values():
			print(value)

def printDicItems(birthday):
	print('---The items of Dic as following:')
	for item in birthday.items():
			print(item)


#对字典进行访问
birthday={'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 14'}
while True:
	print('Enter a name:(Blank to quit)')
	name=input()
	if name=='':
		printDicKeys(birthday)
		printDicValues(birthday)
		printDicItems(birthday)
		break
	if name in birthday:
		print(birthday[name]+' is the birthday of '+name)
	else:
		print('I do not have birthday information for '+name)
		print('what is their birthday')
		bday=input()
		birthday[name]=bday
		print('Birthday database updated')


