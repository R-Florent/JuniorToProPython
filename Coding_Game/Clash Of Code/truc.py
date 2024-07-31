lexicographic =[0,1,2,3,4,5,6,7,8,9]

counter =0
for a in lexicographic:
    for b in lexicographic:
        if b!= a:
            for c in lexicographic:
                if c!= a and c!= b :
                    for d in lexicographic:
                        if d != a and d != b and d !=c :
                            for e in lexicographic:
                                if e != a and e != b and e != c and e!=d:
                                    for f in lexicographic:
                                        if f != a and f != b and f != c and f !=d and f !=e:
                                            for g in lexicographic:
                                                if g != a and g != b and g != c and g != d and g != e and g!=f:
                                                    for h in lexicographic:
                                                        if h != a and h != b and h != c and h != d and h != e and h!=f and h !=g:
                                                            for i in lexicographic:
                                                                if i != a and i != b and i != c and i != d and i != e and i!=f and i!=h and i!=g and i!=h:
                                                                    for j in lexicographic:
                                                                        if j != a and j != b and j != c and j != d and j != e and j!=f and j!=h and j!=g and j!=h and j !=i:
                                                                            counter +=1
                                                                            if counter == 1_000_000:
                                                                                print([a,b,c,d,e,f,g,h,i,j])