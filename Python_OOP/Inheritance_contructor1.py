class Father:

    x=5
    y=6

    def summ(self):
        print(self.x+self.y)


class Son(Father):
    def __init__(self):
        print("Son Constructor")


obj=Father()
obj=Son()



