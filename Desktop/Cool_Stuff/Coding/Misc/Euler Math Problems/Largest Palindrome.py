def find_palin():
    palindrome = []
    
    for x in range(100,1000):
        i = 100
        while i < 1000:
            i = i+1
            a = i *x
            b = str(a)
            if a not in palindrome and b == b[::-1]:
                palindrome.append(i*x)
    return max(palindrome)
