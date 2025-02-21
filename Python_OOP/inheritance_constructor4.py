class Father:
    x=20
    y=15

    def __init__(self):
        print("Father Constructor")

    def addmul(self):
        print(self.x+self.y)

class Son(Father):
    def __init__(self):
        super().__init__()  # super().__init__()  Father Constructor Show here when the create son obj
        print("son Constructor")

#obj=Father()
obj=Son()