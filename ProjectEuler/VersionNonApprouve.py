def deficient():
    #pour diviser un nombre
    dic_des_diviseur = {}

    for i in range(1, 29):
        sum_des_diviseur = 0
        for y in range(1, i // 2 + 1):
            if i % y == 0:
                sum_des_diviseur +=y
            if sum_des_diviseur == i :
                print(i,'est un nombre prafait')

def nombres_abondants(limite=28123):
    list_des_nombres_abondant = []
    for i in range(1,limite+1):
        somme_des_diviseur = 0
        for y in range(1, i // 2 + 1):
            if i%y == 0:
                somme_des_diviseur += y
        if i < somme_des_diviseur:
            list_des_nombres_abondant.append(i)
    return list_des_nombres_abondant

def somme_all_nombres_abondants(table, limite=28123):
    list_sum_nombres_abondants = []
    for i in range(len(table)):
        for j in range(i, len(table)):  # Commence à i pour éviter les doublons
            somme = table[i] + table[j]
            if somme <= limite:
                list_sum_nombres_abondants.append(somme)
    return list_sum_nombres_abondants

abondants = nombres_abondants()
somme_abondants = somme_all_nombres_abondants(abondants)

print("je passe au gros")
indise = 0
somme =0
for i in range(1, 28124):  # Inclure 28123
    if i not in somme_abondants:
        somme += i

print(somme)