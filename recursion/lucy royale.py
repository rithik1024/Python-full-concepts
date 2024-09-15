from random import randint
def luckyroyale(attempt=1):
    number=randint(1,20)
    if number==13:
        print(f"it took {attempt} attempts")
        return None
    attempt+=1
    luckyroyale(attempt)
    
print(luckyroyale())