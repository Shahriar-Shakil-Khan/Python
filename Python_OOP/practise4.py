class Myclass:
    x=5
    y=5

    @staticmethod
    def addSum():
        sum=Myclass.x+Myclass.y
        print(sum)

Myclass.addSum()


# obj=Myclass()
# print(obj.y)
# obj.addSum()

print(Myclass.x)