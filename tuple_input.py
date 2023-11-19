list=[]
inputIn=int(input("Enter how much element you want to enter in tuple"))
for i in range(inputIn):
    user_input=input()
    list.append(user_input)
tuple=tuple(list)
print(tuple)
def reverseTuple(tuples):
    rev_tupple=tuple[::-1]
    return rev_tupple
print(reverseTuple(tuple))