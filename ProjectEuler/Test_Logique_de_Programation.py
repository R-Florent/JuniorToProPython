list = [1,2,3,4]
list_multiple =[]
for i in range(len(list)):
    for y in range(i,len(list)):
        list_multiple.append(list[i]+list[y])

print(list_multiple)
