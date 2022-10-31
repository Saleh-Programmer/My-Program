# from itertools import count
import os

os.system("cls")


def reverse (inputList):
    primary_int_list=[]
    for i in inputList:
        try:
            # comment: for input int value to process
            primary_int_list.append(int(i))
        except :
            continue
        # END TRY
    reverse_list=[]
    for j in range(len(primary_int_list)):
        reverse_list.append(primary_int_list[-1-j])
    print(reverse_list)


reverse(input("Please enter a valid list to reverse:"))