'''write a program to print palindrome of a stringl'''
s=input("ENTER THE STRING:")
if s[::-1]==s:
    print(s+" string is palindrome")
else:
    print(f"{s} string is not palindrome")
