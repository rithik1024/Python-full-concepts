def main():
 with open (r"file handling\sample.log.txt") as f:
    records=[]
    for line in f:
        clean_line=line.strip()
        if clean_line:
            records.append(clean_line)
 return records
print(main())

def message():
    messages=[]
    new=[]
    data=main()
    for item in data:
        messages=data.strip()
        new.append(item[2].strip())
    return new
print(message())