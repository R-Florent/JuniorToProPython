def crible_eratosthene(limite):
    # Initialiser une liste de booléens : True signifie "potentiellement premier"
    est_premier = [True] * (limite + 1)
    est_premier[0] = est_premier[1] = False  # 0 et 1 ne sont pas premiers

    # Parcourir les nombres pour marquer les multiples
    for i in range(2, int(limite**0.5) + 1):
        if est_premier[i]:
            for multiple in range(i * i, limite + 1, i):
                est_premier[multiple] = False

    # Retourner une liste des nombres premiers
    return [num for num, premier in enumerate(est_premier) if premier]

# Fonction pour vérifier si un nombre est premier
def est_premier(nombre, crible):
    return nombre in crible


def is_truncatable(n):
    str_n = str(n)
    str_n_reverse = str_n[::-1]
    for i in range(len(str_n)):
        if not est_premier(int(str_n[i:]), crible):
            continue
        else:
            print(n,"est un cifrepremier")

    for i in range(len(str_n_reverse)):
        if not est_premier(str_n_reverse[:i], crible):
            continue


limite = 1000
crible = crible_eratosthene(limite)
for e in crible:
    is_truncatable(e)