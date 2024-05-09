# Dictionary initial
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Liste des clés à utiliser
l1 = ['A', 'C', 'F']

# Initialisation du nouveau dictionnaire
new_dict = {}

# Itération sur chaque clé dans la liste l1
for key in l1:
    # Ajout de la paire clé-valeur au nouveau dictionnaire
    new_dict[key] = d1[key]

# Ajout d'une nouvelle paire clé-valeur au nouveau dictionnaire
new_dict['G'] = 71

print(new_dict)
