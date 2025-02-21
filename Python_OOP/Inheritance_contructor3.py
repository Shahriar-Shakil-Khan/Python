class Father:
    x=20
    y=15

    def __init__(self):
        print("Father Constructor")

    def addmul(self):
        print(self.x+self.y)

class Son(Father):
    def __init__(self):
        print("son Constructor")

#obj=Father()
obj=Son()