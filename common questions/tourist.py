"""WAPT  return state  from database  to help tourists by taking city name as input"""
Karnataka={"Banglore","Hasan","Mysore"}
Tamilnadu={"chennai","coinbathore","ooty"}
Maharashtra={"pune","Mumbai","Nagpur"}


country= input("Enter the country name which you want to vist:")
if country=="india":
    city=input("Enter the city name you want to visit:")
    if city in Karnataka:
       print("welcome to Karnataka")
    elif city in Tamilnadu:
        print("welcome  to tamil nadu ")
    elif city in Maharashtra:
        print("welcme to maharashra")
else:
    print("country is outside india ")
