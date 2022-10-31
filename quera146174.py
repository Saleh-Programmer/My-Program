# https://quera.org/contest/assignments/43442/problems/146174
# آزمون ورودی سامرکمپ دیوار (بخش اول)
# دو رقمی های اول رشته
input_string=input()

tmpData=[]
for char in input_string:
    if char.isdigit():
        tmpData.append(char)
    else:
        tmpData.append("/")

tmpData = "".join(tmpData)
clearData=tmpData.split("/")


def isAval(num):
    if num>=11:
        for i in range(3,9):
            x=num%i
            if x==0:
                return False
    else:
        for i in range(3,num-1):
            x=num%i
            if x==0:
                return False
    return True

i=0
j=2
def do(in_string):
    if len(in_string)>=2:
        x=in_string[i:j]
        x=int(x)
        if isAval(x):
            print(x)
        else:
            do(in_string[i+1:j+1])
            

for item in clearData:
    if item.isdigit():
        tmpList=item
        do(tmpList)    
                
