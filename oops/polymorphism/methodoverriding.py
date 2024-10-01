class one():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def meth1(self):
        print(f'my name is {self.name} and age is {self.age}')
class two(one):
    def __init__(self,age,name):
        super().__init__(age,name)
    def meth1(self):
        print(f"hello world {self.name} {self.age}")
obj=two('rithik',23)   
obj.meth1()    