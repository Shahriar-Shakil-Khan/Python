from abc import ABC,abstractclassmethod

class Bangladesh(ABC):
    @abstractclassmethod
    
    def show_1_to_10(self):
        pass
    
    @abstractclassmethod
    def show_10_to_20(self):
        pass    
    
    def show_20_to_30(self):
        for i in range(31):
            print(i)
   

class Dhaka(Bangladesh):
    
    def show_1_to_10(self):
         for i in range(10):
            print(i)
   
    def show_10_to_20(self):
        for i in range(20):
            print(i)



obj=Dhaka()
obj.show_1_to_10()
obj.show_10_to_20()
obj.show_20_to_30()