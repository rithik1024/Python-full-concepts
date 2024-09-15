
"""def rithik():
 print("hello world")
 return "hi"
rithik()
print(rithik())
a=[2,1,4,67,4]
a=set(a)
b=a.sort()
print(b)
Example: Sorting a list in ascending order"""

# numbers = [5, 2, 9, 1, 5, 6]
# b=sorted(numbers)
# print(b)
# def add(a,b):
#     return a+b
# for _ in range(0,5): #throw away keyword
#     print(add(3,4))

def greet(name,debug=False,reverse=False):
    if debug:
        print("Calling greet function")
    if reverse:
        return f"hello {name[::-1]}"
    
    return name
print(greet("steve",True,True))
