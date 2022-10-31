
import os
os.system("cls")

class Stack_sample:
    def __init__(self,stack=[],data=None) -> None:
        self.data=data
        self.stack=stack
        
    def set_data_in_stack(self,data):
        self.stack.append(data)
        
    def get_data_from_stack(self):
        if len(self.stack)>0:
            toSend=self.stack[-1]
            self.stack=self.stack[:-1]
            return toSend
        else:
            return None

aTower=[1,2,3]
bTower=[]
cTower=[]

def honoviTower(a,b,c):
    # def showData():
        
    a,b,c=Stack_sample(a),Stack_sample(b),Stack_sample(c)
    
    c.set_data_in_stack(a.get_data_from_stack())
    print(f"aTower now is: {a.stack}")
    print(f"bTower now is: {b.stack}")
    print(f"cTower now is: {c.stack}")
    print("---------------------")
    b.set_data_in_stack(a.get_data_from_stack())
    print(f"aTower now is: {a.stack}")
    print(f"bTower now is: {b.stack}")
    print(f"cTower now is: {c.stack}")
    print("---------------------")
    b.set_data_in_stack(c.get_data_from_stack())
    print(f"aTower now is: {a.stack}")
    print(f"bTower now is: {b.stack}")
    print(f"cTower now is: {c.stack}")
    print("---------------------")
    c.set_data_in_stack(a.get_data_from_stack())
    print(f"aTower now is: {a.stack}")
    print(f"bTower now is: {b.stack}")
    print(f"cTower now is: {c.stack}")
    print("---------------------")
    a.set_data_in_stack(b.get_data_from_stack())
    print(f"aTower now is: {a.stack}")
    print(f"bTower now is: {b.stack}")
    print(f"cTower now is: {c.stack}")
    print("---------------------")
    c.set_data_in_stack(b.get_data_from_stack())
    print(f"aTower now is: {a.stack}")
    print(f"bTower now is: {b.stack}")
    print(f"cTower now is: {c.stack}")
    print("---------------------")
    c.set_data_in_stack(a.get_data_from_stack())
    print(f"aTower now is: {a.stack}")
    print(f"bTower now is: {b.stack}")
    print(f"cTower now is: {c.stack}")
    print("---------------------")
 
  
print(f"aTower first is: {aTower}")
print(f"bTower first is: {bTower}")
print(f"cTower first is: {cTower}")

print("---------------------")
print("---------------------")
    
honoviTower(aTower,bTower,cTower)