from inheritance1 import watsapp_v1
class h2(watsapp_v1):
    def __init__(self, phno, username,video):
        super().__init__(phno, username)
        self.video=video
    def check(self):
        return f"phno is {self.phno}, username is {self.username}, video {self.video}"
obj= h2(2413532,"hikku","not available")
print(obj.check())
obj.chat()