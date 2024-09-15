"""WAPT to check whtether the students is in database or not """
database={7038:"Steve",6300:"Jack Shepard",7795:"Kate",6098:"Swayer",8861:"Hugo reeves",9995:"jacob",7449:"Charlie"}
reg_no=int(input("Eneter the register number:"))
if reg_no in database:
    sub=input("Enter the subject:")
    if sub=="python":
        print(f"Mr/mrs {database[reg_no]} you are welcome to {sub} class")
    elif sub=="SQL":
        print(f"Mr/Mrs {database[reg_no]}you are welcome to {sub}  class")
    else:
         print("sub not available")
else:
        print("contact your counsilor")
