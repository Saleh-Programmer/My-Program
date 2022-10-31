# https://quera.org/contest/assignments/43442/problems/146176
# آزمون ورودی سامرکمپ دیوار (بخش اول)
# جزیره گنج

size_matrix = int(input())

# get data from input and store them in a list
matrix = []
for rows in range(size_matrix):
    row = map(int, input().split())
    matrix.append(list(row))

# find any node of data in matrix that have 1 and store the address of them in a list
rawData = []
row = 0
column = 0
for itemInEachMatrixList in matrix:
    for item in itemInEachMatrixList:
        if item == 1:
            rawData.append((row, column))
        column += 1
    row += 1
    column = 0

# this function remove any node of data that haven't rule of competition
resultList=[]
def check(item):
    i, j = item
    if (i, j+1) in rawData:
        resultList.append(item)
        resultList.append((i,j+1))
    else:
        if (i+1, j) in rawData:
            resultList.append(item)
            resultList.append((i+1,j))
        else:
            pass

# run function for each data in rawData list
for node in rawData:
    check(node)

# main portion of algorithm is here
# first I find witch row or column is max or equal

countDicRow = {}
countDicColumn = {}
resultList=set(resultList)
resultList=list(resultList)
for item in resultList:
    x, y = item
    if x in countDicRow.keys():
        countDicRow[x] += 1
    else:
        countDicRow[x] = 1

for item in resultList:
    x, y = item
    if y in countDicColumn.keys():
        countDicColumn[y] += 1
    else:
        countDicColumn[y] = 1


tmpRawData = set(resultList).copy()
countMax = 0
tmpCountMaxRow = 0
tmpCountMaxColumn = 0
if max(countDicRow.values()) > max(countDicColumn.values()):
    for item in countDicRow.items():
        if item[1] == max(countDicRow.values()):
            columnF = item[0]
            for item in tmpRawData:
                x, y = item
                if x == columnF:
                    countMax += 1
                if y == x:
                    continue
                # else:
                #     if y == columnF:
                #         countMax += 1


elif max(countDicRow.values()) == max(countDicColumn.values()):
    for item in countDicRow.items():
        if item[1] == max(countDicRow.values()):
            columnF = item[0]
            for item in tmpRawData:
                x, y = item
                if x == columnF:
                    tmpCountMaxRow += 1
                if y == x:
                    continue
                # else:
                #     if y == columnF:
                #         tmpCountMaxRow += 1
    for item in countDicColumn.items():
        if item[1] == max(countDicColumn.values()):
            columnF = item[0]
            for item in tmpRawData:
                x, y = item
                if y == columnF:
                    tmpCountMaxColumn += 1
                if x == y:
                    continue
                # else:
                #     if x == columnF:
                #         tmpCountMaxColumn += 1
    countMax = max([tmpCountMaxColumn, tmpCountMaxRow])

else:  # max(countDicRow.values()) < max(countDicColumn.values())
    for item in countDicColumn.items():
        if item[1] == max(countDicColumn.values()):
            columnF = item[0]
            for item in tmpRawData:
                x, y = item
                if y == columnF:
                    countMax += 1
                if x == y:
                    continue
                # else:
                #     if x == columnF:
                #         countMax += 1

print(countMax)
