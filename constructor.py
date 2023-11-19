class s:
    def printHello(self):
        print("Hello "+self.name)
class ss(s):
    def printHello2(self):
        print("i am hello 2")

obj2=ss()
obj2.printHello2()
obj2.name="aman"
obj2.printHello()