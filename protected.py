class Lpu:
    __y=32
    def __init__(self,student,fac) :
         self.student=student
         self.fac=fac
    
    def infoPrint(self):
         print("Students in LPU:",self.student)
         print("Fac in LPU:",self.fac)

obj=Lpu(50000,2000)
obj.infoPrint()
print(obj.student)
obj._Lpu__y=11
print(obj._Lpu__y)



