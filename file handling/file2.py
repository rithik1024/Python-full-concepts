def read_log():
  record=[]
  with open(r"C:\Users\Rihthik Raj\Documents\Qspiders-python\file handling\access-log.txt","r") as f:
       for line in f:
           clean_line=line.strip()
           if clean_line:
               record.append(clean_line)
          # print(line)
  return record
  
def ip_address():
    ip=[]
    data=read_log()
    for item in data:
        word=item.split()
        ip.append(word[0])
    return ip

data = ip_address()
for i in data:
    print(i)       
    
def unique_ip():
   unique_ip=[]
   data=ip_address()
   for item in data:
       if item not in unique_ip():
           unique_ip.append(item)
   return unique_ip

def count_ip_adress():
    data=ip_address()
    count_ip={}
    for item in data:
        count_ip[item]=data.count(item)
    return count_ip

data =count_ip_adress()
d=sorted(data.items(),key=lambda args :args[-1],reverse=True)
d_={}
for item in d:
    d_[item[0]]=item[-1]
print(d_)


        