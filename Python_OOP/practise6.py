class Father:
    x=10
    y=20

    def __init__(self):
        print("Father Constructor")

    def addSum(self):
        print(self.x+self.y)


class Son(Father):
    pass


obj=Son()