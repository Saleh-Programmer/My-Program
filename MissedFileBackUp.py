from tkinter import *
from tkinter import filedialog
import os.path , os,datetime,sys ,pytz
from persiantools.jdatetime import JalaliDate
from datetime import datetime

root = Tk()
root.iconbitmap(PhotoImage("H:\My programming Code\.vscode\My Projects\Graphical Find Missed Files\data-backup.ico"))
root.title("برنامه شناسایی نواقص بایگانی ")

global lbl_introduce
lbl_introduce = Label(root, text="با سلام و عرض احترام ، این نرم افزار جهت شناسایی فایل های بایگانی نشده تهیه شده است. ", justify=RIGHT,pady=20).grid(row=0 , column=1, columnspan=4, )
lbl_introduce1 = Label(root, text=".کافی است اولین و آخرین فایلی که باید بایگانی بشود را بایگانی کرده و این نرم افزار را اجرا کنید ", justify=RIGHT,pady=10).grid(row=1 , column=1, columnspan=4)
btnEnterFolderAddress = Button(text="انتخاب پوشه حاوی فایل های بایگانی "  ,command= lambda: operation(),padx=5,bg="yellow",fg="black",borderwidth=1,pady=10).grid(row=2 , column=0,columnspan=2)


global txtReport
txtReport= Text(root,pady=10,borderwidth=1,bg="lightblue")

def operation():
    folder = filedialog.askdirectory()
    today=JalaliDate.today()
    try:

        list_sample= os.listdir(f"{folder}")

    except FileNotFoundError:
        os.system("cls")
        folder=input("Please enter correct address:")
        try:
                list_sample= os.listdir(f"{folder}")
        except:
                sys.exit()

    main_list=[]

    # get file type that is purpose of this app
    file_type="txt"


    # this lines is used to filter files
    numberEX=len(file_type)+1
    try:
        for list in list_sample:
                if list.endswith(f".{file_type}") and isinstance(int(list[:-numberEX]), int) :
                    main_list.append(list)
                else:
                    continue
    except :
        pass


    if len(main_list)==0:
        sys.exit()
    else:
        new_list=[]
        for i in main_list:
                new_list.append(int(i[:-numberEX]))
        new_list.sort()
        missed_list=[]
        min=new_list[0]
        max=new_list[-1]
        for i in range(min,max):
                if i in new_list:
                    continue
                elif i>min:
                    missed_list.append(i)


        def better_report(list):
                os.system("cls")
                now=datetime.now()
                reportTime=now.strftime("%Y , %m , %d")
                s_list=[]
                registeFile= open(f"{folder}\\Missed Files {today}.txt","w")
                for i in list:
                    if i+1 in list:
                            s_list.append(i) 
                    else:
                            if s_list != []:
                                try:
                                        registeFile.write(f"{s_list[0]} --> {i} ({len(s_list)+1})\n")
                                except: pass
                                s_list.clear()
                            else:
                                registeFile.write(f"{i}\n")
                registeFile.close()

        better_report(missed_list)


        registeFile= open(f"{folder}\\Missed Files {today}.txt","r")
        report = registeFile.read()
        txtReport.insert(END,report)
        txtReport.grid(row=6,columnspan=4)

        lbl_result = Label(root, text=".گزارش کسورات بایگانی بشرح ذیل است یک نسخه از این گزارش در پوشه بایگانی ذخیره شده است" ,fg="blue",padx=10 ,pady=5,font="size:14 ").grid(row=3 , column=3)
        txtExit= Button(root, text="خروج",command=lambda : sys.exit(),padx=5,width=20,bg="green",borderwidth=1).grid(row=7)
        lblProgrammerInfo =  Label(root, text=f"Programmer: Saleh13611397@gmail.com",fg="blue",pady=5,font="size:14 ").grid(row=7 , column=3)
        btnEnterFolderAddress = Button(text="انتخاب پوشه حاوی فایل های بایگانی " ,padx=5,bg="yellow",fg="black",borderwidth=1,pady=10).grid(row=2 , column=0,columnspan=2)

root.mainloop()
