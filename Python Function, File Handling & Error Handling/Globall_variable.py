x=10  #Global Variable
y=20  #Global Variable

def myfun():
    print("Local Answer : ",x+y)

myfun()
print("Global Answer : ",x+y)
