class GrandFather:
    x=100
    y=200
    a=6
    b=3

    def addSum(self):
        print(self.x + self.y)

    def subSum(self):
        print(self.x - self.y)

    def mulSum(self):
        print(self.a * self.b)

    def divSum(self):
        print(self.a / self.b)

class Father(GrandFather):
    pass

class Son(Father):
    pass


obj=Son()
print(obj.x)
print(obj.y)

obj.addSum()
obj.subSum()
obj.mulSum()
obj.divSum()