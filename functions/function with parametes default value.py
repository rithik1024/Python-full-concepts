def spam():
    print("hey spam")
    return 10
for _ in range(0,1):
    print(spam())

def greet(name,debug=False,reverse=False):
    if debug==True:
        print(f"{name} executing greet function")
    if reverse==True:
        print("running")
    return name
print(greet("rithik",debug=True))
