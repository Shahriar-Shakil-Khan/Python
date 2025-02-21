class GrandFather:
    a=45
    b=5

    def sum(self):
        answer1=self.a+self.b
        print(answer1)

    def sub(self):
        answer2 = self.a - self.b
        print(answer2)

    def mul(self):
        answer3 = self.a * self.b
        print(answer3)

    def div(self):
        answer4 = self.a / self.b
        print(answer4)


class Father(GrandFather):
    pass

class Son(Father):
    pass

#obj=GrandFather()
#obj=Father()
obj=Son()
print(obj.a)
print(obj.b)
obj.sum()
obj.sub()
obj.mul()
obj.div()

