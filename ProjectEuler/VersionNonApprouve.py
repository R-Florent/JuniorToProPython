def nombres_abondants(limite=28123):
    list_des_nombres_abondant = []
    for i in range(1, limite + 1):
        somme_des_diviseur = 0
        for y in range(1, i // 2 + 1):
            if i % y == 0:
                somme_des_diviseur += y
        if i < somme_des_diviseur:
            list_des_nombres_abondant.append(i)
    return list_des_nombres_abondant

def somme_all_nombres_abondants(table, limite=28123):
    set_sum_nombres_abondants = set()  # Utiliser un set pour éviter les doublons
    for i in range(len(table)):
        for j in range(i, len(table)):  # Commence à i pour éviter les doublons
            somme = table[i] + table[j]
            if somme <= limite:
                set_sum_nombres_abondants.add(somme)
    return set_sum_nombres_abondants

# Trouver tous les nombres abondants jusqu'à 28123
abondants = nombres_abondants()

# Trouver toutes les sommes de deux nombres abondants
somme_abondants = somme_all_nombres_abondants(abondants)

# Calculer la somme de tous les nombres qui ne peuvent pas être écrits comme la somme de deux nombres abondants
somme = 0
for i in range(1, 28124):  # Inclure 28123
    if i not in somme_abondants:
        somme += i

print(somme)
