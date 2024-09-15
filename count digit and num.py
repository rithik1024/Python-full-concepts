s="hai 123 python23"
digit_count=0
str_count=0
for i in s:
    if s.isdigit():
        digit_count+=1
    elif s.isalpha():
        str_count+=1
print(str_count)
print(digit_count)