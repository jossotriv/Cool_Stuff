#def prime_sum(x):
#     range_of_num = [val for val in range(2,x)]
#     for i in range(len(range_of_num)):
#         if range_of_num[i] != 0:
#             print(range_of_num[i])
#             a= 1
#             while a - range_of_num[i] < len(range_of_num):
#                 range_of_num[a] = 0
#                 a += range_of_num[i]
#                 if a  >= len(range_of_num):
#                     if range_of_num[a-range_of_num[i]] % i == 0:
#                         range_of_num[a-range_of_num[i]] =0
#     return sum(range_of_num)

# #all factors of 2 equal zero
# def sum_prime(x):
#     a = [val for val in range(x)]
#     for i in range(len(a)):
#         for x in range(len(a)):
#             if x+i < len(a):
#                     if (x +i) % 2 == 0:
#                             a[x+i]=0
#             elif x+ i==len(a):
#                     if a[x] %i == 0:
#                         a[x]=0
#     #print(a)
#     return sum(a)
import math
def prime_sum(x):
	b = [True]*x
	b_limit = math.sqrt(x) 
	for n in range(4,x,2):
		b[n] = False
	for t in range(3,x,2):
		if b[t]:
			for m in range(t**t,t,2*t):
				b[m] = False
	sum_ = 0
	for i in range(2,x):
		if b[i]:
			sum_+= b[i]
	return sum_
