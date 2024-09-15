#without using inbuilt function  check whhether the sring is palindrome or not

s=input("enter the element:")
'''
if s[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print(f"{s}  is uppercase")
else:
    print(f"{s} is not uppercase")'''

if "A"<=s[0]<="Z":
    print(f"{s} is an uppercase")
else:
    print(f"{s} not an uppercase")