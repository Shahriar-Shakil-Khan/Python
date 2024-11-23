with open ("nana/example.text","w") as file:
    print("created")
'''

with open ("nana/example.text","w") as file:
    file.write("Hello!Shakil,How Are you man?")


with open ("nana/example.text","r") as file:
    x=file.read()
    print(x)

os.rename("nana","No")

os.remove("No/example.text")
os.rmdir("No")
'''
