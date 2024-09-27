from inheritance2 import watsapp_v2
class watsapp_v3(watsapp_v2):
    def __init__(self,phno,username,profile,about):
        super().__init__(phno,username,profile)
        self.about=about
    def status(self):    
        return (f"About of {self.username} is '{self.about}'- profile picture:{self.profile}")

obj=watsapp_v3(6238961518,"brad pitt","brad.jpg","live in the moment")
print("------------------------------------------------------------------------")
print(obj.status())
print("------------------------------------------------------------------------")  