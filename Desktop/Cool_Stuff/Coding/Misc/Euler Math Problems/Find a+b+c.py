def find(x):
    for n in range(x):
        for i in range(x):
            for l in range(x):
                if n + i + l == 1000 and (n**2 + i**2 == l **2 or  n**2 + l**2 == i**2 or l**2 + i**2 == n**2) and n!= i and i!=l and n!= l:
                    return "n= "+str(n) +", i = "+ str(i) +", l = "+ str(l)
