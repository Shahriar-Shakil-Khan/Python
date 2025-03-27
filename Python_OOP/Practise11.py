#public access modifier

class Car:
    Brand="BMW"

    def BrandName(self):
        print(f"Car Brand Name is {self.Brand}")


class Motor(Car):
    def ChildBrandName(self):
        print(f"Car Brand Name is {self.Brand}")


obj=Motor()
obj.BrandName()
print(obj.Brand)
