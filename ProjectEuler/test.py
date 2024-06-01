import math
import pprint
def matrixH0(k):
    H0 = []
    for m in range(k):
        # create a new row
        row = []
        for n in range(k):
            if abs(m-n)==1:
                row.append(math.sqrt(n+m+1)/2.)
            else:
                row.append(0)
        H0.append(row)
    return H0
pprint.pprint(matrixH0(4))