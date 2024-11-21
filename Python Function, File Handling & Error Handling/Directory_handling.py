#create directory
'''
import os
os.mkdir("new")
'''

'''
import os
result=os.listdir("new/.")
print(result)

import os

with open ("new/test.text","w") as file:
    file.write(" Shakil")
    

import os

os.rename("new","new1")

import os
os.remove("new1/test.text")
os.rmdir("new1")
'''

import os
x=os.listdir("text")
#print(x)

for x1 in x:
    print(x1)


