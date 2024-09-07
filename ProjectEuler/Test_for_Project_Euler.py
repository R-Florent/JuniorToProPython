list_resulte = []
res = 0
for a in range(2, 5+1):
    for b in range(2, 5+1):

        res = a ** b
        if res in list_resulte:
            print('cette valeur est déja dans la liste', res)
        list_resulte.append(res)

list_resulte = sorted(list_resulte)

print(list_resulte)