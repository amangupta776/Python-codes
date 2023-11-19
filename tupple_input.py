inputNum=input("Enter values you want to enter in Tupple and using , for seprate:")
list=inputNum.split(",")
tuple=tuple(list)
print(tuple)
for i in tuple:
    print(i)
new_tuple=tuple*3
print("New tuple:")
for i in new_tuple:
    print(i)