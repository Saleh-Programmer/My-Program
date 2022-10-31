# برنامه نویس : محمد صالح رستمی
# saleh13611397@gmail.com
# gitHub: https://github.com/Saleh-Programmer
# linkedin: https://www.linkedin.com/in/mohammad-saleh-rostami-6b13451a4
# حل تمرین سایت کوئرا
# https://quera.org/problemset/148640/   متن سوال
# https://quera.org/problemset/148640/submissions/ نتیجه داوری

# توضیحا با توجه به اینکه در سوال مطروحه شیوه ورود اطلاعات مشخص نشده بود بنده اطلاعات را از یک فایل متنی می خوانم
# سپس در صورت صحت فرمت اطلاعات نسبت به تصحیح اقدام می نمایم


# import os

# os.system("cls")  # پاک کردن ترمینال در هربار اجرای برنامه

# خواندن فایل پاسخ نامه
# with open(input("Please enter quiz answer address: "), 'r') as f:
# RawInformation = f.readlines()


# ورود اطلاعات از ترمینال
runApp = True
rawInformation = []
while runApp:

    if line := input():
        rawInformation.append(line)
    else:
        runApp = False


def cleaningData():  # (/n ) پاکسازی دیتای ورودی از کارکترهای کنترل مثل

    global totalQuestion   # تعداد سوالات
    global answerKey  # کلید سوالات
    global totalUser   # تعداد پاسخ نامه
    global usersAnswer  # پاسخ نامه
    global answerKeyDic

    mainKey = []  # جهت ذخیره سازی اطلاعات پالایش شده پاسخنامه
    for item in rawInformation:
        if item != rawInformation[-1]:
            mainKey.append(item)
        else:
            mainKey.append(item)

    totalQuestion = int(mainKey[0])
    answerKey = mainKey[1]
    totalUser = mainKey[2]
    usersAnswer = mainKey[3:]


def result(usersAnswer):  # تصحیح آزمون
    userScore = 0
    iterUser = totalQuestion
    i = j = 0
    for answer in usersAnswer[i:iterUser]:
        answerTemp = answerKey[i:iterUser][j]
        if answerTemp == "A":
            if answer[0] == "#":
                userScore += 3
        elif answerTemp == "B":
            if answer[1] == "#":
                userScore += 3
        elif answerTemp == "C":
            if answer[2] == "#":
                userScore += 3
        elif answerTemp == "D":
            if answer[3] == "#":
                userScore += 3
        j += 1
    i += iterUser
    print(userScore)
    # return(userScore)


def start():  # بررسی صحت اطلاعات داده شده
    cleaningData()
    i = 0
    if int(totalQuestion) == len(answerKey) and \
            len(usersAnswer) % int(totalUser) == 0:
        for user in range(1, int(totalUser)+1):
            result(usersAnswer[i:user+int(totalQuestion)+i])
            i += int(totalQuestion)
    else:
        ("Your input data is not in correct format.")


start()  # شروع برنامه

# 1
# A
# 1
# #OOO
