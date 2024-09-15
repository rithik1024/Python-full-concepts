from datetime import datetime
class invalidage(Exception):
    pass
def civil_service(year):
    age=datetime.now().year-year
    
    try:
        if age>=21 and age<=35:
            print("you are eligible for civil service exam")
        else:
            raise invalidage
    except invalidage:
        print("your age is not valid and you can't appear for civil service examination")          
year=int(input("enter your birth year:"))
civil_service(year)