def find_prime(x):
    divisor = x
    primes= []
    counter = 0
    for i in range(2,divisor+1):
        counter+=1
        if divisor % i ==0:
            primes.append(i)
            while divisor % i == 0:
                divisor = divisor/i
            if divisor == 1:
                return max(primes)
    return max(primes)
