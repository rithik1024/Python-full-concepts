s="Apple is a fruit"
vowels=set()
for char in s:
    if char in "aeiouAEIOU":
        vowels.add(char)
        
print(vowels)
vowels_={char for char in s if char in "AEIOUaeiou"}
print(vowels_)