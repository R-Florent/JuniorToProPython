list_coin = [1,2,5,10,20,50,100,200]


way = []
list_de_way = []
s=0
compteur = 0
i = 0
#for e in range(0,len(list_coin)):
while s < 200:
    s = s + list_coin[0+i]
    way.append(s)

if way == list_de_way[compteur -1]:
    i += 1
list_de_way.append(way)

