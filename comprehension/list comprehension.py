# language=["python ","peral","c","java"]
# li=[i for i in language if i[0] in "Pp"]
# print(li)
names=["Jack","Swayer","clarie","james","aadith","john locke"]
#cons_=[i for i in names if i[0] not in "aeiou"]
new=[name for name in names if len(name)<7]
print(new)