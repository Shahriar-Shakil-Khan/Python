class Father:
    x=5
    y=5

    def addTwoFather(self):
        return self.x+self.y

class Son(Father):
 def addTwoSon(self):
     sum = self.addTwoFather()+100
     print(sum)



obj=Son()
# obj=Father() # Father can not access it
obj.addTwoSon()