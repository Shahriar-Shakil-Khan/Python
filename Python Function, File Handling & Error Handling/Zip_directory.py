import os
import zipfile

with zipfile.ZipFile("No/new.zip","w") as zip:
    zip.write("No/1.text")
    zip.write("No/2.text")
    zip.write("No/3.text")

