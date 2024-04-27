from math import *
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


#exponent(base, exp)


a= 2
b=-1
c= -6
"""a = int(input())
b = int(input())
c = int(input())"""


def calcul_f_seconde_degrée(coeficein_direvteur, coeficein_b, chiffre):
    b_carre = (coeficein_b * coeficein_b)
    quatreac = 4 * coeficein_direvteur * chiffre
    delta = b_carre - quatreac
    print("la valeure de est :", delta)
    solution1 = 0
    solution2 = 0
    if delta > 0:
        print("il y a alors 2 solution :")
        solution1 = (sqrt(delta) - coeficein_b) / (2 * coeficein_direvteur)
        solution2 = (- sqrt(delta) - coeficein_b) / (2 * coeficein_direvteur)
        print(solution1,solution2)

    elif delta == 0:
        print("il y a alors 1 solution :")
        solution1 = (-coeficein_b) / (2 * coeficein_direvteur)
    else:
        print("il n'y a pas de solution")

calcul_f_seconde_degrée(a,b,c)