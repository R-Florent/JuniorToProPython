def collastz_sequence_test(n=1,nb_iterations=10):
    liste_de_liste = [[] for _ in range(nb_iterations)]

    def generate_collatz_sequences(n, current_iteration):
        if current_iteration == nb_iterations:
            return

        n_pair = 2 * n
        n_impaire = (n - 1) / 3

        liste_de_liste[current_iteration].append(n_pair)

        if n_impaire % 2 != 0 and n_impaire.is_integer():
            liste_de_liste[current_iteration].append(int(n_impaire))

        generate_collatz_sequences(n_pair, current_iteration + 1)

        if n_impaire % 2 != 0 and n_impaire.is_integer():
            generate_collatz_sequences(int(n_impaire), current_iteration + 1)

    generate_collatz_sequences(n, 0)
    return liste_de_liste


print(collastz_sequence_test())