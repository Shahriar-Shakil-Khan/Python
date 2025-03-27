#private access modifier

class Car:
    __Brand="BMW"

    def BrandName(self):
        print(f"Car Brand Name is {self.__Brand}")


class Motor(Car):
    def ChildBrandName(self):
        print(f"Car Brand Name is {self.__Brand}")


obj=Car()
obj.BrandName()

# obj=Motor()
# obj.ChildBrandName()

