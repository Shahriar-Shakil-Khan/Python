import os
#os.mkdir("No")
'''
with open("No/1.text","w") as file:
    print("created")

with open("No/2.text","w") as file:
    print("created")

with open("No/3.text","w") as file:
    print("created")
'''

x=os.listdir("No")
#print(x)

for x1 in x:
    print(x1)