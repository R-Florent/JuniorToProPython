def deficient():
    #pour diviser un nombre
    dic_des_diviseur = {}

    for i in range(1, 29):
        sum_des_diviseur = 0
        for y in range(1, i // 2 + 1):
            if i % y == 0:
                sum_des_diviseur +=y
            if sum_des_diviseur == i :
                print(i,'est un nombre prafait')



deficient()
