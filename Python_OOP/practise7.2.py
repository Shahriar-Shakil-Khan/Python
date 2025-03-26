class Father:
    x=5
    y=5

    def addTwoFather(self):
        print(self.x+self.y)

class Son(Father):
    def addTwoSon(self):
        print(self.x+self.y)


obj=Son()
# obj=Father() # Father can not access it
obj.addTwoSon()