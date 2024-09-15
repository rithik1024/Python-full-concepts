"""o/p
[1,2]
[2,3]
.
.
.
[7,8]
[9]
"""
num=[1,2,3,4,5,6,7,8,9]
print(num[0:5])
for i in range(0,len(num),2):
    print(num[i:i+2])