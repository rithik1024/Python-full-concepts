num=int(input("Enter the element:"))
if 0<=num<=9:
    print(f"number {num} is single digit")
elif 10<=num<=99:
     print(f" {num} is two digit number ")
elif 100<=num<=999:
    print(f" {num} is three digit number")