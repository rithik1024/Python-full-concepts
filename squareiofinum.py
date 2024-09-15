"""wapt check the square of the given number is even or odd
if it is even print  "good morning"  else orint good eveneing"""

num=int(input("enetr the number:"))
if (num**2)%2==0:
    print(f"{num} is even ")
else:
    print("number is odd")

