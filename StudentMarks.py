class studentMarks:
    def __init__(self,english,soft,python,mth):
        self.english=english
        self.mth=mth
        self.soft=soft
        self.python=python
    # def __init__(self,id,name):
    #     self.name=name
    #     self.id=id
   
    def calculate(self,name,id):
        self.total=(self.english+self.mth+self.soft+self.python)//4
        print("Studen name is",name,"and student id is",id)
        print("Total Average Marks of Student is",self.total)

name=input("Enter Student name:")
id=int(input("Enter Student id:"))
english=int(input("Enter English Marks:"))
soft=int(input("Enter Soft Skill Marks:"))
python=int(input("Enter Python Marks:"))
mth=int(input("Enter Maths Marks:"))
obj=studentMarks(english,soft,python,mth)
obj.calculate(name,id)

