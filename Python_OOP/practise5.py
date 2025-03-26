#single Inheritance

class Father:
    x=1000
    y=500

    def addSum(self):
        print(self.x+self.y)

    def subSum(self):
        print(self.x-self.y)

class Son(Father):
    pass

#
# obj=Father()
# print(obj.x)
# print(obj.y)
# print(obj.addSum())
# print(obj.subSum())

obj=Son()
obj.addSum()
obj.subSum()