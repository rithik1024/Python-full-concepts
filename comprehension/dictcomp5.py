# Buildings
buildings = {
'burj khalifa': 828,
'Shanghai_Tower': 632,
'Abraj_Al_Bait_Clock Tower': 601,
'Ping_An_Finance_Centre_Shenzhen': 599,
'Lotte World Tower': 554.5,
'World Trade Center': 541.3
}
#1 meter=3.28

buildings_={}
for build,height in buildings.items():
   buildings_[build]=str(height*3)+" feet"
print(buildings_)
#buildings_={build:str(height*3)+" feet"  for build,height in buildings.items()}
#print(buildings)