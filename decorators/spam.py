def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def mul (a,b):
   return a*b

def calculator(opcode,a,b):
    if opcode==1:
        return add(a,b)
    if opcode==2:
        return sub(a,b)
    if opcode==3:
        return mul(a,b)
    else:
        return "Unknown Operartor"

print(calculator(5,2,3))

