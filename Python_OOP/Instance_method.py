class Myclass:
    x=20
    y=30

    def __init__(self,zValue,yValue):
        self.z=zValue
        self.y=yValue

    def addTwo(self):
        sum=self.x+self.y+self.z
        print(sum)


obj=Myclass(100,80)
print(obj.z)
print(obj.y)
obj.addTwo()