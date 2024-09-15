s="this is a bunch of code"
new=s.split()
dir ={ i:len(i) for i  in new  if len(i)%2==0 }
print(dir)

