def positive(func):
    def wrapper(*args):
        res=func(*args)
        return abs(res)
    return wrapper
@positive
def sub(a,b,c):
    return a-b-c

print(sub())