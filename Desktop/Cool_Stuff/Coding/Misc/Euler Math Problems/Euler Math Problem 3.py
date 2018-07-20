600851475143
list_of_primes=[]
n = 1
while n <600851475143:
    n+=1
    if 600851475143 % n == 0:
        for i in list_of_primes:
            if n % i != 0:
                list_of_primes.append(n)
    print(list_of_primes)
    print(n)
    print(600851475143 % n )
    
print( list_of_primes)
    
