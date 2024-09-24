class employee:
    location='europe'
    def __init__(self,name,company,sal):
        self.name=name
        self.company=company
        self.sal=sal
    def details(self):
         return (f"my name is {self.name}\n"
                fmy company is {self.company}\n"
                f"sal is {self.sal}")
obj=employee('rithik','newtechnology',30000)
print(obj.details())    
