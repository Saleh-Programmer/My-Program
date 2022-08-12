# Programmer : Mohammad Saleh Rostami (saleh13611397@gmail.com)
# Programm name: X-O game
# Version: 1.0
# Date Created: 2022/08/13



import os , random
os.system("cls")

choiceList = ["11","12","13","21","22","23","31","32","33"]
winnerList =[("11","12","13"),("21","22","23"),("31","32","33"),("11","22","33"),("13","22","31"),("11","21","31"),("12","22","32"),("13","23","33")]
winnerListSet= set(winnerList)
userListDictionary={"computer":[],"user":[]}
userShape="   #  "
computerShape="   *  "

pictureDrawingInformation={"11":["11"],
                           "12":["12"],
                           "13":["13"],
                           "21":["21"],
                           "22":["22"],
                           "23":["23"],
                           "31":["31"],
                           "32":["32"],
                           "33":["33"]
                           }


def inputValidation(value):
    if value in choiceList:
        return True
    else:
        return False
    

def computerAction():
    computerChoice= random.choice(choiceList)
    choice = choiceList.index(computerChoice)
    userListDictionary["computer"].append((choiceList.pop(choice)))
    pictureDrawingInformation[computerChoice]=computerShape
    print(f"Computer's choice is : {computerChoice}")
    draw()
    check_winner()
    

def userAction():
    userChoice = input("What's your choice: ")
    if inputValidation(userChoice):
        choice=choiceList.index(userChoice)
        userListDictionary["user"].append((choiceList.pop(choice)))
        pictureDrawingInformation[userChoice]=userShape
        check_winner()
    else:
        print("Enter correct choice...")
        userAction()
    
    
def draw():
    print("----------------------------------------")
    print(f"-  {pictureDrawingInformation['11']}   -  {pictureDrawingInformation['12']}    -  {pictureDrawingInformation['13']}    -")
    print("----------------------------------------")
    print(f"-  {pictureDrawingInformation['21']}   -  {pictureDrawingInformation['22']}    -  {pictureDrawingInformation['23']}    -")
    print("----------------------------------------")
    print(f"-  {pictureDrawingInformation['31']}   -  {pictureDrawingInformation['32']}    -  {pictureDrawingInformation['33']}    -")
    print("----------------------------------------")
    
def check_winner():
    for item in winnerList:
        if set(item).issubset(userListDictionary["user"]) :                    
            print(f"User Win .... ")
            draw()
            exit()
        elif set(item).issubset(userListDictionary["computer"]) :                    
            print(f"Computer Win ....")
            draw()
            exit()
            
       
def action():
    draw()
    while True:
        userAction()
        computerAction()


# -----------------------------------------------------
action()