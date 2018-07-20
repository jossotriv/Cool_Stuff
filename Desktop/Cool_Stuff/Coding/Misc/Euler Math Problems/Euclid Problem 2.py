def fib(number):
	if number == 0:
		return 0
	if number == 1:
		return 1
	else:
		return fib(number-1)+fib(number-2)
sum_ = 0
n = 0
while fib(n) < 4000000:
	if fib(n) % 2 == 0:
	    sum_ += fib(n)
	n+=1
	print(fib(n))
print("done")
print(sum_)
