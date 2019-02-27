#exersize1
def listTransper(lstparam):
	last = lstparam[-1]
	newlast='and '+str(last)
	lstparam[-1]=newlast
	i=0
	len_lstparam=len(lstparam)
	returnvalue=''
	while i<len_lstparam:
		if	(i+1)<len_lstparam:
			returnvalue+=str(lstparam[i])+', '
		if	(i+1)==len_lstparam:
			returnvalue+=str(lstparam[i])
		i+=1

	print(returnvalue)

#listTransper(['a','b','c'])
listTransper(['a','b','c',5,6,7])

#exersize2
grid=[['.','.','.','.','.','.'],
		['.','0','0','.','.','.'],
		['0','0','0','0','.','.'],
		['0','0','0','0','0','.'],
		['.','0','0','0','0','0'],
		['0', '0', '0', '0', '0', '.'],
		['0', '0', '0', '0', '.', '.'],
		['.', '0', '0', '.', '.', '.'],
		['.','.','.','.','.','.'],
	  ]

row=len(grid)
col=len(grid[0])
for i in range(0,col):
	a=''
	for j in range(0,row):
		a+=str(grid[j][i])
	print(a,end='\n')









