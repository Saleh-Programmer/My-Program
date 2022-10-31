
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


aTower=Stack_sample(list(range(int(input("Enter number of ring: ")),0,-1)))
bTower=Stack_sample([])
cTower=Stack_sample([])

def honoviTower(a,b,c):
    rule=a.stack
    if len(b.stack)==0 and len(c.stack)==0:    
        while c.stack!=rule:
            c.set_data_in_stack(a.get_data_from_stack())
            b.set_data_in_stack(a.get_data_from_stack())
            b.set_data_in_stack(c.get_data_from_stack())
            c.set_data_in_stack(a.get_data_from_stack())
            a.set_data_in_stack(b.get_data_from_stack())
            c.set_data_in_stack(b.get_data_from_stack())
            c.set_data_in_stack(a.get_data_from_stack())
       

    print(f"aTower now is: {a.stack}")
    print(f"bTower now is: {b.stack}")
    print(f"cTower now is: {c.stack}")
    print("---------------------")
    print("---------------------")
    print("---------------------")
print("\n\n")  
print(f"aTower first is: {list(aTower.stack)}")
print(f"bTower first is: {list(bTower.stack)}")
print(f"cTower first is: {list(cTower.stack)}")

print("---------------------")
print("---------------------")
    
honoviTower(aTower,bTower,cTower)