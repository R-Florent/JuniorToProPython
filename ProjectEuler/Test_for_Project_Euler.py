import math

def is_prime(n):
    for diviseur in range(2,int(math.sqrt(n)) + 1,2):
        if n % diviseur == 0:
            return False
    return True

compteur = 0
max_n =0

for a in range(-1000,1000):
    for b in range (-1000,1000):
        n = 0
        suite = n**2+a*n+b
        while is_prime(suite) == True:
            suite = n**2+a*n+b
            n +=1
            print(n)

        if max_n < n:
            max_n =n