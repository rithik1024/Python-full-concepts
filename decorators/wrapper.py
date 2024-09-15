from time import sleep

def span(func):
    def wrapper(*args):
        sleep(1)
        return func(*args)
    return wrapper

@span  # greet = span(greet)
def greet():
    return   "hello world"

def greeting(name):
    return f"hello {name}"
print(greet())
