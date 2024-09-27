class student:
    inst="pyspiders"
    
    def __init__(self,name,age,phno):
        self.name=name
        self.age=age
        self.phno=phno
        
    def details(self):
        return (f"My name is {self.name} \n"
        f"my age is {self.age} \n"
        f"my phno is {self.phno} \n"
        f"my institue is {student.inst}")    
        
obj=student('Rithik',21,6238961518)
# print(obj.details())

print(student.inst)
print(obj.inst)
print(obj.name)
#print(student.name)   we cant acess instance attrubute by using class name 
# print("-----")
# print(student('rithik',23,234).details())#calling detals  function in class by using class name -----no prefered---

