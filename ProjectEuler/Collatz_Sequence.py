from time import sleep

nb_iterations = 10

liste = [[] for _ in range(nb_iterations+1)]

cache = {}


def test(n, iteration):
    if n in cache:
        return
    cache[n] = None
    liste[nb_iterations-iteration].append(n)

    iteration -= 1
    if iteration == -1:
        return

    n_pair = 2 * n
    n_impaire = (n - 1) / 3

    test(n_pair, iteration)

    if n_impaire.is_integer() and (n_impaire % 2) == 1:
        test(int(n_impaire), iteration)

test(1, nb_iterations)


print(liste)
unique_result = []
for row in liste:
    unique_result += row

unique_result = sorted(set(unique_result))
print(unique_result)
print(len(unique_result))
