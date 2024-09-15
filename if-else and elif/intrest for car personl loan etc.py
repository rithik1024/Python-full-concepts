""""write a program to return intrest amount for the loan amount based on the loan type there are three different types of loan
1)car loan 11% intrest
2)personal loan  9 %
3)house loan   7%"""

loan_amount=int(input("Enter the loan amount:"))
print("options\n"
      "please eneter 1 for personal loan\n"
      "please enter 2 for car loan\n"
      "please enter 3 for house loan")

option=int(input("Enter your option:"))
if option ==1:
       intrest=loan_amount*.11
       print(f"loan amount is {loan_amount} ")
       print(f"Amount with intrest is {intrest+loan_amount} ")
elif option==2:
       intrest=loan_amount*.09
       print(f"loan amount is {loan_amount} ")
       print(f"Amount with intrest is {intrest+loan_amount} ")
elif option==3:
       intrest=loan_amount*.07
       print(f"loan amount is {loan_amount} ")
       print(f"Amount with intrest is {intrest+loan_amount} ")
else:
       print("Invalid option")

    