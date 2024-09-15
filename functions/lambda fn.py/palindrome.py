pal =lambda string: f"{string} is palindrome" if string==string[::-1] else "not" 
print(pal("jack"))