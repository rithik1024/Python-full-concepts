""" wapt for college counciling """

engineering=["ME","EEE",'CSE',"ECE","IT","CH"]
per=int(input("Enter your percentage :"))
name =input("Enter your name:")
if per >75:
    if per> 85:
        print(f"Dear { name} you are eligible to take\n {"\n".join(engineering)}")
        option=input("Enetr  the option:")
        if option in engineering:
            print(f"welcome to {option} course ")
        else:
             print(f"sorry {option} not in database")
    else:
        print(f" dear {name} you are eligible to take"
              f"{"\n".join(engineering[3::])}")
        option=input("Eneter your option:")
        if option in engineering[3::]:
             print(f"{name } welcome to the course")
        else:   
            print(f"{option } not in database")
else:
    print(f"dear {name} you are not eligible to take enginnering course")
  