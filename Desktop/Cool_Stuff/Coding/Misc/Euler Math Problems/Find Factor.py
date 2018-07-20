def find_prime_factorization(x):
    divisor = x
    primes= []
    counter = 0
    for i in range(2,divisor+1):
        
        if divisor % i ==0:
            counter = 0
            while divisor % i == 0:
                counter+=1
                divisor = divisor/i
            primes.append(i**counter)
            if divisor == 1:
                return primes
    return primes
def find_factors():
    factors = []
    for x in range(2,21):
        for i in range(len(find_prime_factorization(x))):
            if find_prime_factorization(x)[i] not in factors:
                factors.append(find_prime_factorization(x)[i])
    return factors
def find_greatest_common_factors():
    factors = find_factors()
    for t in range(len(factors)):
        i = t
        while i < len(factors):
            i +=1
            if i == len(factors):
                break
            if factors[i] % factors[t] ==0 and factors[i]!=factors[t]:
                factors.remove(factors[t])               
    return factors
def lcm():
    factors = find_greatest_common_factors()
    mult= 1
    for a in range(len(factors)):
        mult *= factors[a]
    return mult
        
