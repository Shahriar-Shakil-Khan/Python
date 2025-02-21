
class Myclass:
    x=10
    y=20

    def __init__(self):   #without constructor
        sum=self.x+self.y
        print(sum)

obj = Myclass()


class Myclass:
    x=10
    y=20

    def __init__(self,a,b):
        sum=self.x+self.y+a+b  #with constructor
        print(sum)

obj = Myclass(10,10)
















