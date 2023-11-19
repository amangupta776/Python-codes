class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print("Name is", self.name)
        print("Age is", self.age)


class child(Super):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.name = name
        self.age = age

    def printInfo(self):
        super().printInfo()
        print("Child Name is", self.name)
        print("Child Age is", self.age)


obj = child("aman", 22)
obj.printInfo()
