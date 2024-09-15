# nums=[1,2,3,4,5,6,7,8,9,10]
# fnum=nums[0]
# lnum=nums[-1]
# fnum,*middle,lnum=nums
# print(fnum,lnum,middle)
l=[i for i in range(1,21)]
print(*l)
fnum=[0]
fnum,*mid=l
print(fnum,fnum,mid)
#print(l)

def  fun(name,age,pay):
    return ( f"hello {name} you are {age} years old and you will get pay {pay}")
data=["steve",24,7000]
print(*data)
print(fun(*data))
