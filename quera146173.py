# https://quera.org/contest/assignments/43442/problems/146173
# آزمون ورودی سامرکمپ دیوار (بخش اول)
# رمزنگاری رشته

str_input=input()
hash_data={}
for char in str_input:
    if char in hash_data.keys():
        hash_data[char]+=1
    else:
        hash_data[char]=1
for item in hash_data.items():
    key,value=item
    print(f"{value}{key}",end="")    
    