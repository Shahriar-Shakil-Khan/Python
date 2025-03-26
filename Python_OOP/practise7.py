class Father:
    x=10
    y=40

    @staticmethod
    def addSum():
        print(Father.x+Father.y)

class Son(Father):
    pass


obj=Son()
obj.addSum()

obj=Father()
obj.addSum()