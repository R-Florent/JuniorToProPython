dividande = 1
diviseur = 7

restes = []
while dividande != 0:
    dividande = (dividande * 10) % diviseur
    if dividande in restes:
        print(f"Cycle détecté avec un reste de {dividande}")
        break
    restes.append(dividande)

print("Les restes rencontrés : ", restes)
