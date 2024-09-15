#check given data is  is string or not if it if string print how many characters it have else print the value
 
data= eval(input("enetr the data:"))
if type (data)==str:
    print(str(len(data))+ " is the numbe rof characters")
else:
    print(data)