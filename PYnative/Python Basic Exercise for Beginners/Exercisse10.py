list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []

# Ajouter les éléments pairs de list1 à new_list
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        new_list.append(list1[i])

# Ajouter les éléments impairs de list2 à new_list
for i in range(len(list2)):
    if list2[i] % 2 != 0:
        new_list.append(list2[i])

print(new_list)
