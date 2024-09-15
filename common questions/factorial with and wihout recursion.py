n=int(input("enetr the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# from math import factorial
# num=int(input("enter the input"))
# print(factorial(num))

def fact5():
    return 5*fact4()
def fact4():
    return 4*fact3()
def fact3():
    return 3*fact2()
def fact2():
    return 2*fact1()
def fact1():
    return 1

print(fact5())

def rfact(n):
    if n<=0:
        return None 
    #base case
    if n==1:
        return 1
    #Recursive case
    return n*rfact(n-1)
print(rfact(100))