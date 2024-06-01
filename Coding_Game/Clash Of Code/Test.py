import sys
from math import *

nb = 126
l =[]
for i in range(2,nb):
    l += [2**i]
l = l [::-1]

for e in l:
    if nb >= e :
        print(e)
        break

print(l)