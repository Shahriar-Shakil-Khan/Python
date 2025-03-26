class Father:
   pass

class Son(Father):
    x = 10
    y = 40

    @staticmethod
    def addSum():
        print(Son.x + Son.y)


# obj=Son()
# obj.addSum()

obj=Father()     # it donot run the code cause father can not access from his Son prpperty
obj.addSum()

