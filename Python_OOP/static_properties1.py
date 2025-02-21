class Myclass:
    a=20
    b=5

    @staticmethod
    def summation():
        sum=Myclass.a+Myclass.b
        print(sum)

print(Myclass.a)
print(Myclass.b)
Myclass.summation()