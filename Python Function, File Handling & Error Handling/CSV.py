import csv
'''
data=[
[1,	"Level 1",	"AA	Agriculture", "Forestry and Fishing","Dollars (millions)",	"H01",	"Total income",	"Financial performance"	,"54462",	"ANZSIC06 division", "A"],
[2,	"Level 2",	"BB	CSE", "Computer","Dollars (millions)",	"H02",	"Total income",	"Financial performance2"	,"544621",	"ANZSIC06 division2", "B"],
[3,	"Level 3",	"BB	CSE", "Computer","Dollars (millions)",	"H02",	"Total income",	"Financial performance2"	,"544621",	"ANZSIC06 division2", "B"]

]

with open("new.csv","w") as file:
    csv_file=csv.writer(file)
    csv_file.writerows(data)
    print("CVS file Create Successfully")
    
'''
data=[]
with open("new.csv","r") as file:
    content=csv.reader(file)
    for row in content:
        data.append(row)

print(data)