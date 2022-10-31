num_input = int(input())
sum = 0
for item_input in range(num_input):
    tempList=input().split()
    intTempList = [int(i) for i in tempList]
    if intTempList[0]<intTempList[1]:
        sum+=intTempList[0]
    else:
        sum+=intTempList[1]

print(sum)
    