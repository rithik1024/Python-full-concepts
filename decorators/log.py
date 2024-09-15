def log(func):
    def wrapper(*args):
      print(f"you are calling  {func.__name__} funtion")
      return func(*args)
    return wrapper
@log 

def greeting(name):
    return "hello world"

print(greeting("rithik"))