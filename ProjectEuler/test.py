dic = {2: 3, 3: 2, 7: 2}
def generate_combinations(dic):
    prime_number = list(dic.keys())
    results = []

    def all_diviseur(index_dic,current):

        if index_dic >= len(prime_number):
            results.append(current.copy())
            return

        prime_key = prime_number[index_dic]
        max_exponent = dic[prime_key]

        for exponent in range(max_exponent+1):
            current.append(prime_key ** exponent)
            all_diviseur(index_dic + 1, current)
            current.pop()

    all_diviseur(0,[])
    return results

def list_all_diviseur():
    diviseur = []
    combinations  = generate_combinations(dic)
    for combi in combinations:
        product = 1
        for number in combi:
            product *= number
            diviseur.append(product)
    return diviseur

for g in list_all_diviseur():
    print(g)