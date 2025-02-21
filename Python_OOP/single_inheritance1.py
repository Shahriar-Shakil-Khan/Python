class Father:
    x=8
    y=10

    def sub(self):
        print(self.x-self.y)

    def div(self):
        print(self.x/self.y)


class Son(Father):
    pass

obj=Son()
print(obj.x)
print(obj.y)
obj.sub()
obj.div()


