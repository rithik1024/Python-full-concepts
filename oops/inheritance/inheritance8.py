from inheritance6 import h1
from inheritance7 import h2

class hybrid(h1,h2):
    def __init__(self, phno, username, audio,video):
        super().__init__(phno, username, audio,video)