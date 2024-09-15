"""Building a dictionary whose price value is more than 200"""
prices ={'ACME': 45.23,
      'AAPL': 612.78,
      'IBM': 205.55,
      'HPQ': 37.20,  'FB':10.75}

# prices_={}
# for key,val in prices.items():
#      if val>200:
#          prices_[key]=val
# print(prices_)

prices_={key:val for key,val in prices.items() if val>200}
print(prices_)