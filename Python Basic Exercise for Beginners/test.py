base = 2
exp = 5


def exponent(base, exp):
    print("base = ", base)
    print("exp =", exp)
    produit = 1
    affichage = "i.e.("
    for i in range(exp, 0, -1):
        produit = produit*base
        affichage = affichage + f"{base}*"
    affichage = affichage[0:-1]
    affichage += f") = {produit}"

    print(base, "raises to the power of", exp, "is :", produit,affichage)


exponent(base, exp)