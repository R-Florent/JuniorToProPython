def puissance_5(n):
    print(n ** 5)
resulta =0

for nombre in range(1633, 354294):
    str_nombre = str(nombre)
    somme_a_la_puissance = 0
    for e in str_nombre:
        somme_a_la_puissance += int(e) ** 5
    if somme_a_la_puissance == nombre:
        print(somme_a_la_puissance)
        resulta += somme_a_la_puissance

print(resulta)