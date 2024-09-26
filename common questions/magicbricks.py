num=input("Enter the number:")
sum=0
def magic(num,sum):
 for i in range(0,len(num)):
    num=int(num)
    var=num%10
    sum+=var
    num/10
 if sum==1:
    print("its a magic number")
 else :
    return magic(num/10)
print(magic(num))
 