character=int(input("Enter num of words"))
list=[]
for variable in range(0,character):
    variable=input()
    list.append(variable)
print(list)
print(list[len(list):0:-1])