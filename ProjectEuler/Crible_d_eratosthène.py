def crible_eratosthène_2026(n):
    L = [True] * n
    L[0] = False
    L[1] = False
    for i in range(2,n):
        if L[i]:
            for j in range(i*i,n,i):
                L[j] = False
    return [e for e in range(n) if L[e]==True]

print(crible_eratosthène_2026(120))