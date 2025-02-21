class Myclass:
    x=50
    y=60

    @staticmethod
    def addTwo():
        sum=Myclass.x+Myclass.y
        print(sum)

Myclass.addTwo()

obj=Myclass()
obj.addTwo()