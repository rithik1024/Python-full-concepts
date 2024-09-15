"""write a program to check the character is uppercase or not if it is lowercse convert it into uppercase esle print the same"""

data=input("Enter the string:")
# if data.isupper():
#     print(data)
# else:
#     print(data.upper())

if "a"<= data<="z":
    for i in range(0,len(data)):
     cap=chr(ord(data[i])-32)
     l=[]
     l.append(i)
     print(" ".join(l))
else:
    print(data)