def find_prime(x):
    n = 3
    prime_count = 1
    prime=[2]
    prime_t = False
    if x <1:
        return "You stupid ho"
    while prime_count != x:
        n+=1
        prime_t = True
        for t in prime:
            
            if n % t == 0:
                prime_t = False
        if prime_t:
            prime_count +=1
            prime.append(n)
    return max(prime)
