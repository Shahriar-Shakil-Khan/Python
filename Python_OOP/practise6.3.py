class Father:
    x=10
    y=20

    def __init__(self):
        print("Father Constructor")

    def addSum(self):
        print(self.x+self.y)


class Son(Father):

    def __init__(self):
        super().__init__()
        print("Son Constructor")


obj=Son()
