import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for diviseur in range(3, int(math.sqrt(n)) + 1, 2):
        if n % diviseur == 0:
            return False
    return True


compteur = 0
max_n = 0
max_a=0
max_b=0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        while True:
            suite = n * n + a * n + b
            if suite <= 0 or not is_prime(suite):
                break
            n += 1

            if max_n < n:
                max_n = n
                max_a = a
                max_b = b
print(max_n,max_b*max_a)
