# https://quera.org/contest/assignments/43442/problems/146172
# آزمون ورودی سامرکمپ دیوار (بخش اول)
# قطرهای ماتریس

lenMat = int(input())
matrix = []
rawData = []

for item in range(lenMat):
    tmpMatrix = list(map(int, input().split()))
    matrix.append(tmpMatrix)

i = j = 0
for i in range(lenMat):
    rawData.append(matrix[i][j])
    j += 1
    rawData.append(matrix[i][-j])

sum = 0
for x in set(rawData):
    if (x-1) % 3 == 0:
        sum += x

print(sum)
