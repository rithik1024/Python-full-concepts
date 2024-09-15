"""WAP to replace words in a string"""
string="hi how are you"
words=string.split()
s=""
for i in words:
 if i=="how":
  s+="who"+" "
 else:
     s+=i+" "
print(s)