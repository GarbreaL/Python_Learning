lstNames = [["a", "b", "c"], ["aa", "bb", "cc"]]
for i in range(len(lstNames)):
	print("names index =" + str(i) + " and name is " + str(lstNames[i]))

index_a = lstNames[0].index("a") ;  # 有时候双引号的字符不能被找到，要用单引号才行

print(index_a)




