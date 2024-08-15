len_of_recurence_max = 0

for diviseur in range(2,1000,1):
    flag = True
    len_of_recurence =0
    dividande = 1%diviseur

    while flag == True:
        reste = dividande % diviseur
        dividande = reste*10
        len_of_recurence += 1
        if reste == dividande:
            flag = False

        if reste ==0:
            flag = False

    if len_of_recurence_max < len_of_recurence:
        len_of_recurence_max = len_of_recurence

    print(len_of_recurence)

print(len_of_recurence_max)