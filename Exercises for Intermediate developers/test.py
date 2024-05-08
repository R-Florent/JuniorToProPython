sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
new_list = []

for e in sample_list:
    if sample_list.count(e) > 1 and e not in new_list :
        new_list.append(e)
print(new_list)
