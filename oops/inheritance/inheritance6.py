from inheritance1 import watsapp_v1
class h1(watsapp_v1):
    def __init__(self, phno, username,audio):
        super().__init__(phno, username)
        self.audio=audio
    def check(self):
        return f"phno is {self.phno}, username is {self.username}, audio {self.audio}"
obj= h1(2413532,"hikku","available")
print(obj.check())
obj.chat()