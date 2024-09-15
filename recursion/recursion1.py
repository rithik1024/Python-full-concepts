def funcOne():
    a=1
    result=a+ funTwo()
    return result

def funTwo():
    a=2
    result=a+funThree()
    return result
def funThree():
    a=3
    return a
print(funcOne())