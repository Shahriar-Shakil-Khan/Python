# Multiple Inheritance

class Father:
    x=100
    y=200

    def addSum(self):
        print(self.x + self.y)

    def subSum(self):
        print(self.x - self.y)

class Mother:
    a = 6000
    b = 1000

    def mulSum(self):
        print(self.a * self.b)

    def divSum(self):
        print(self.a / self.b)

class Son(Father,Mother):
    pass


obj=Son()
print(obj.x)
print(obj.y)
print(obj.a)
print(obj.b)

obj.addSum()
obj.subSum()
obj.mulSum()
obj.divSum()

