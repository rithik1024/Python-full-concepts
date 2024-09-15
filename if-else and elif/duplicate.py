'''write a program to remove duplicates if given  value is collection (list,tuple,set,str), 
else prit reversed value '''

data = eval(input("Enter the data: "))
if isinstance(data,(str,list,tuple,set,dict)):
    conv= set(data)
    print(conv)
else:
    new=str(data)
    new1=new[::-1]
    print(f"{new1}  is the reversed data")
