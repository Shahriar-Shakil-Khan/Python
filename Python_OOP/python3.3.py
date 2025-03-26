class Myclass:
    x=10
    y=20

    def __init__(self,zValue):
        self.z=zValue

    def addSum(self):
        sum=self.x+self.y+self.z
        print(sum)


obj=Myclass(70)
obj.addSum()


