# Dial Codes
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
    ]
#o/p:{"china":86,"india":91,....}
# for item in  dial_codes:
#     di[item[1]]=item[0]
# print(di)
di={item[-1]:item[0] for item in dial_codes}
print(di)