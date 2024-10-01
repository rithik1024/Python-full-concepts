from inheritance4 import watsapp_v2
from inheritance1 import watsapp_v1

class whatsapp_v3(watsapp_v1,watsapp_v2):
    def __init__(self,audio,phno,address):
        self.audio=audio
        self.phno=phno
        self.address=address
    def wats(self):
        return f" voice call {self.audio} , phno is {self.phno}  address is {self.address}"
obj=whatsapp_v3("available",4851686116," kottyam")
print(obj.wats())