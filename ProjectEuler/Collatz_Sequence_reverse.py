nb_iteraction = 10

liste_de_liste =[]

for e in range(nb_iteraction):
    liste_de_liste.append([])


def collastz_sequence_test(n=1, nb_iteraction=10):
    for e in liste_de_liste:
        n_pair = 2 * n
        n_impaire = (n - 1) / 3

        e.append(n_pair)
        if n_impaire%2 !=0 and n_impaire%2 == int():
            e.append(n_impaire)
        if nb_iteraction ==0:
            return liste_de_liste
        nb_iteraction -=1
        for element in liste_de_liste[nb_iteraction]:
            collastz_sequence_test(element)

print(collastz_sequence_test())