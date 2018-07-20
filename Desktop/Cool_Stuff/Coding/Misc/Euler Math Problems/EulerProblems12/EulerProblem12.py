# #Solution 1- works by counting the factor for every number; very slow
# number = 0
# divisors = 0
# counter = 1
# while divisors < 500:
#     divisors =0
#     number += (counter)
#     divider = number
#     while divider > 0:
#         if number % divider ==0:
#             divisors +=1
#         divider -=1
#     counter+=1
#     print('Finished number: ' + str(number) + " and it has "+str(divisors)+ " divisors")
# print(divisors)
# print(number)
# #Solution 2 - find the prime factorization for every number and then sum the exponents and multiply them so that we can find the number of factors
# number = 0
# divisors = 0
# counter = 1
# while divisors <500:
#     number +=1
#     #use sieve of arestothenes to find prime factors of each number, only need to check up to sqrt(number) for prime factors

# if you find the prime factorrs for a number and the quantity of each unique one, then you can multiply the number of unique primes  +1 by each other
# Ex.:
    # 9 = {3:2)
    # factors = (2+1) * 1 = 3 factors = 3,1,9
    # 12 = {2:2,3:1}
    # factors = (2+1) * (1+1) = 6 factors = 2,4,6,12,3,1

# find the factors of the triangle numbers,
# this triangle number o
print('hey')