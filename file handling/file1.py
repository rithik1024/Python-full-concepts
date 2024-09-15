with open (r"C:\Users\Rihthik Raj\Documents\Qspiders-python\file handling\movies.txt","r") as file :
       print(file)
       print(type(file.read()))
       for line in file:
        print(line.strip())
       r=(next(file))
       row=[]
       row=next(file)
       for i in row:
              print(row)