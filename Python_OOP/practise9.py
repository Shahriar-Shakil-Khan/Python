from abc import ABC,abstractclassmethod

class Bangladesh(ABC):
    @abstractclassmethod
    def print0to10(self):
        pass
    
    @abstractclassmethod
    def print11to20(self):
        pass
    
    def print21to30(self):
        for i in range(30):
            print(i)


class Dhaka(Bangladesh):
    
    def print0to10(self):
        for i in range(10):
            print(i)
        
    
    def print11to20(self):
        for i in range(20):
            print(i)

          



obj=Dhaka()
obj.print0to10()
print("...")
obj.print11to20()
print("...")
obj.print21to30()