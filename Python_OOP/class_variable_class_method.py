class Myclass:
    x=10
    y=20
    z=30

    def addTwo(self,a,b,c):
        sum=self.x+self.y+self.z +a +b +c
        print(sum)

    def addNew(self):
        self.addTwo(5,6,1)


obj=Myclass()
obj.addTwo(20,10,10)
obj.addNew()
