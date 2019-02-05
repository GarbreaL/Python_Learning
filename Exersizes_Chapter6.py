"""
printTable 提供一个打印方法，把列表进行排序
"""

def printTable():
    tableData = [['apples', 'oranges', 'cherries', 'banana', 'strawberries'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'mouse', 'goose', 'cow', 'duck', 'chicken', 'hen']]
    dicMaxStringLength={}
    maxItemCount=0
    for i in range(len(tableData)):
        if len(tableData[i])>maxItemCount:
            maxItemCount=len(tableData[i])
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > dicMaxStringLength.get(i, 0)+1:
                dicMaxStringLength[i]=len(tableData[i][j])
    for i in range(maxItemCount):
        strPrint= ''
        for j in range(len(tableData)):
            strTemp = ''
            if i < (len(tableData[j])):
                strTemp = tableData[j][i]

            strPrint=strPrint + strTemp.rjust(dicMaxStringLength[j], '')+' '
        print(strPrint)


print('-----------------------------')

printTable()
print('-----------------------------')

