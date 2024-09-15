from csv import reader
def read_csv():
    with open(r"C:\Users\Rihthik Raj\Documents\Qspiders-python\file handling\employee.csv") as f:
        records = []
        rows = reader( f)# creating an instance of 'reader' function
        headers = next(f) # skipping first record
        expected_types = [str,str,int,str,str]
        for row in rows:
            converted = [expected_type(item) for expected_type,item in zip(expected_types,row)]
            records.append(converted)
    return records
print(read_csv())      
# # what is the total amount that i am paying to all employees as salary
# def total_pay():
#     # read the contents of csv file into python data-structure
#     data = read_csv()
#     _total_pay = 0
#     new=[]
#     for item in data:
#         _total_pay = _total_pay + item[2]
#         new.append(_total_pay)
#     return new

# #print(total_pay())

# def more_3k():
#    more3k=[]
#    data=read_csv()
#    print(data)
#    for item in data:
#         if item[2]>3000:
#           more3k.append(item)
#    return more3k
 
# print(more_3k())

# def count_by_gender():
#     data=read_csv()
#     gender_={}
#     for item in data:
#         print(item)
#         gender=item[3]
#         if gender not in gender_:
#             gender_[gender]=1
#         else:
#             gender_[gender]+=1
#     return gender_

# print(count_by_gender())

