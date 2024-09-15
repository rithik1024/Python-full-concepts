s=eval(input("enter the data:"))
if isinstance(s,(list,dict,set)):
    print(f"{s} is mutable")
else:
    print(f"{s} is not mutable")