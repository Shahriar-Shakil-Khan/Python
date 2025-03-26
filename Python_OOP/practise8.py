class Father:
    x=50
    y=50

    def addSum(self):
        sum=self.x+self.y
        print(sum)

class Son(Father):
    pass

    def addSum(self):
        sum = self.x + self.y +100  # overriding Method
        print(sum)

obj=Son()
obj.addSum()