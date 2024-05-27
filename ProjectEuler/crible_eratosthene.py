def crible_eratosthene_GPT(n):

    premiers = [True] * (n +1 )
    p=2
    while p * p <= n:
        if premiers[p]:
            for i in range(p*p, n+1,p):
                premiers[i] = False
        p +=1
    return [p for p in range(2, n + 1) if premiers[p]]



def crible_eratosthene(n):

    prime = [i for i in range(2,n+1,1)]
    for i in prime:
        if i*i <= n+1:
            for y in prime :
                if y!= i  and y%i == 0:
                    prime.remove(y)
    print(prime)

crible_eratosthene(50)
def crible_eratosthene_clem(n):

    prime = [i for i in range(2, n + 1, 1)]
    for i in prime:
        if i * i <= n + 1:
            prime = [e for e in prime if (e == i or e % i != 0)]

    print(prime)

crible_eratosthene_clem(50)