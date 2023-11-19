my_set={1,2,3,5}
# for i in my_set:
#     print(i)
# my_set.add(6)
# print("after adding 6:")
# for i in my_set:
#     print(i)
# my_set.remove(2)
# print("after removed 2:")
# for i in my_set:
#     print(i)
my_set2={1,2,8,9}
my_set3=my_set.difference(my_set2)
print("after intersection:")
for i in my_set3:
    print(i)