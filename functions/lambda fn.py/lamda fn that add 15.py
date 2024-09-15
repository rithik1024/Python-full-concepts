# def fun(a):
#   print(a+15)
# fun_=lambda a:a+15
# a=fun(10)
# print(fun_(10))

def oddnum(num):
  if num%2==0:
    return f"{num} is even number"
  else:
    return f"{num }is odd number"
evenodd=lambda num: f"{num} is even number " if num%2==0 else "odd"
print(oddnum(200))
print(evenodd(200))