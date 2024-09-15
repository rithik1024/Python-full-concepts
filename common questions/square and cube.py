nums=[1,2,3,4,5,6]
res=map(lambda num:(num**2,num**3),nums)
for i in range(0,len(nums)):
    print(next(res))
    