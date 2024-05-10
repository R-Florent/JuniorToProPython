def saisir_chiffres() -> list:
    user_input = input("Veuillez entrer une série de chiffres : ")
    num_list = [int(char) for char in user_input if char.isdigit()]
    return num_list

def palindrome_num(list):
    list_reverse = list.reverse()
    print(list_reverse)
def test(list):
    if not len(list) % 2 == 0 :
        print("elle est paire")
        for i in list:
            print(list[0,-1])

liste_chiffres = saisir_chiffres()
liste_chiffres_reverse = liste_chiffres.copy()
liste_chiffres_reverse.reverse()

#print("Liste des chiffres saisis :", liste_chiffres)
#print("Liste des chiffres saisis inverse :", liste_chiffres_reverse())

print("original number", liste_chiffres)

if liste_chiffres == liste_chiffres_reverse:
    print("Yes. ",liste_chiffres," was palindrome number")
else:
    print("Non :",liste_chiffres,liste_chiffres_reverse,"wasent palindrome number")

#palindrome_num(liste_chiffres)
#list.index(x[, start[, end]])