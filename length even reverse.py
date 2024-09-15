
a=['apple','orange','google','yahoo','facebook','instagram']
odd_even=[item[::-1] if len(item)%2==0 else len(item) for item in a]
print(odd_even)

