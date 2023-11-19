from abc import ABC,abstractclassmethod
class parent(ABC):
    @abstractclassmethod
    def define(self):
        pass
class child(parent):
    def define(self):
        print("hello")
        
obj=child()
obj.define() 