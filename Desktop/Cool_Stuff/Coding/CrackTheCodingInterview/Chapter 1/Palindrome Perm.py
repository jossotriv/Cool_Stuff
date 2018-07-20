import string as st
def  perm_palindrome(string):
    # print("Starting " + string)
    letters = " ".join(st.ascii_lowercase).split(" ") + " ".join(st.ascii_uppercase).split(" ")
    hash_ = {}
    oddcount = 0

    for i in string:
        if i in letters:
            if i not in hash_:
                hash_[i] = 0
                oddcount +=1
                # print( i +" not in hash_")
            elif i in hash_:
                hash_[i] +=1
                if hash_[i] % 2 == 0:
                    oddcount += 1
                else:
                    oddcount -= 1
                # print(i + " in hash_")

        # print("The current hash table is: ")
        # print(hash_)
        #
        # print("The oddcount is: " + str(oddcount))

    return oddcount <= 1

print(perm_palindrome("hey"))
print("__________________________________________")
print(perm_palindrome('boom'))
print("__________________________________________")
print(perm_palindrome("bab"))
