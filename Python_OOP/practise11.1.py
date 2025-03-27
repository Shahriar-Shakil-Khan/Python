#protected access modifier

class Car:
    _Brand="BMW"

    def BrandName(self):
        print(f"Car Brand Name is {self._Brand}")


class Motor(Car):
    def ChildBrandName(self):
        print(f"Car Brand Name is {self._Brand}")


obj=Motor()
obj.BrandName()


print(obj._Brand)  #not recomended
