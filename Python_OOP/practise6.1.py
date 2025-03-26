class Father:
    x=10
    y=20

    def addSum(self):
        print(self.x+self.y)


class Son(Father):

    def __init__(self):
        print("Father Constructor")



obj=Father()   # father can not get this from his Son