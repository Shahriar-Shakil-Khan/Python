class Father:
    x=100
    y=20

    def summ(self):
        summation=self.x+self.y
        print(summation)

    def sub(self):
        subtraction=self.x-self.y
        print(subtraction)

class Mother:

    a=200
    b=50
    def mul(self):
        multi = self.a + self.b
        print( multi)

    def div(self):
        division = self.a / self.b
        print( division)


class Son(Father,Mother):
    pass

obj=Son()
print(obj.x)
print(obj.y)
print(obj.a)
print(obj.b)

obj.summ()
obj.div()
obj.mul()
obj.sub()
