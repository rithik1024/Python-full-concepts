from inheritance1 import watsapp_v1

class watsapp_v2(watsapp_v1):
    def __init__(self,phno,username,profile):
        self.profile=profile
        super().__init__(phno,username)
    def voice_call(self):
        print(f"calling {self.username}")

obj=watsapp_v2(254622283,"Nibin","mypic.jpg")
obj.voice_call()