#create file

#write read
'''
with open ("example.text","w") as file:
    file.write("Hello,python")

'''


#read file
'''
with open ("example.text","r") as file:
    content=file.read()
    # print(file.read())
    print(content)
'''

'''
#rename
import os
os.rename("example.text","new_example.text")
'''
'''
#remove
import os
os.remove("new_example.text")
'''

import os
os.remove("text/test.text")