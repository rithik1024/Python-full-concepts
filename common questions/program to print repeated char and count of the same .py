s="which would be worse, to live as a monster or to die as a good man"
count_pair={}
for char in s:
    if s.count(char)>1:
        count_pair[char]=s.count(char)
print(count_pair)