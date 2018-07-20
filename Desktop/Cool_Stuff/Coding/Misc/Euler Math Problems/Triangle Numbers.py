#rule to find triangular numbers: N*(N+1)/2
def find_factor_count(x):
    factors=0
    N =1
    i = N
    while N*(N+1)/2 != 1:
        if N*N+1/2 % i == 0:
            factors+=1
        i-=1
    N+=1
    i = N
    if N*(N+1)/2 == 1 and factors == x:
        return N

    
def find_factor(t):
    for  in range(t):
        
