class Father:
    x=100
    y=30

    def addTwo(self):
        sub=self.x+self.y
        print(sub)

    def mulTwo(self):
        mul=self.x*self.y
        print(mul)

class Son(Father):
    pass

obj=Father()
a=obj.x
b=obj.y
print(a)
print(b)
obj.addTwo()
obj.mulTwo()





