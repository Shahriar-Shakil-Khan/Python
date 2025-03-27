# Overloading using Variable length Argument

class Father:
    x=10
    y=80

    def addSum(self,*a):
        print(a)

obj=Father()
obj.addSum(1)
obj.addSum(1,2,6)
