# Overloading using Default Argument

class Father:
    x=10
    y=30
    
    def addSum(self,a=0,b=0):
        print(self.x+self.y+a+b)
    

obj=Father()
obj.addSum(5,6)
obj.addSum(5)