# a=10
# def new():
#     a=a+1
#     return a
# print(new())

def fun():
    a=200
    def wrapper():
        return a+1
    return wrapper()
print(fun())

def new():
    result= a+b  
    a=100
    b=200
    return result
    
print(new())