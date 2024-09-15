"""building a list of first name and last name from full names"""


full_names=["steve jobs","bill gates","john doe","tim cook"]
fname=[]
lname=[]
# for name in full_names:
#     fname.append(name.split()[0])
#     lname.append(name.split()[1])
fname=[i.split()[0] for i in full_names]
lname=[i.split()[1] for i in full_names]
print(fname)
print(lname)