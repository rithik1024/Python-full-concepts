"""WAPT PPrint result by taking mocks of 4 subjects [90-1-00]:distinction, 75-90: first class,50-75:second class,0-50:fail """

res1=int(input("Enter the score  of sub 1: "))
res2=int(input("Enter the scores of sub 2: "))
res3=int(input("Enter the scores of sub 3: "))
res4=int(input("Enter the scores of sub 4: "))
tot=(res1+res2+res3+res4)/4
if 100>=tot>=90:
    print("Distnction")
elif 90>=tot>=75:
    print("First class")
elif 0<=tot<=50:
    print("Fail")