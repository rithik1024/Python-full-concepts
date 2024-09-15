"""index raised as power of the item"""

a=[1,2,3,4,5]
power=[]
# for i,j in enumerate(a):
#     power.append(j**i)
power=[j**i for i,j in enumerate(a)]
print(power)
