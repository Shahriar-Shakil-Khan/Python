import zipfile
import os

#os.mkdir("yes")

'''
with open("yes/one.text","w") as file:
    print("created")

with open("yes/two.text","w") as file:
    print("created")
    
with zipfile.ZipFile("yes/yes1.zip","w") as zip:
    zip.write("yes/one.text")
    zip.write("yes/two.text")
with zipfile.ZipFile("yes/yes1.zip","r") as zip:
    zip.extractall()
    ex_file=zip.namelist()
    print(ex_file)
'''
import shutil
shutil.make_archive("Yes_yes","zip","yes")





