class overload:
    def add(self,a,b,c=None):
        if(c==None):
            print("Adding Two Number:",a+b)
        else:
            print("Adding Three Number:",a+b+c)

         


obj=overload()
obj.add(11,12)
obj.add(11,12,1)
