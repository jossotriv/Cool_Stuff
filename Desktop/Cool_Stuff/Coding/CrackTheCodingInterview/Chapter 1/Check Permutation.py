def is_perm(string1,string2):
    hash_ = {}
    for i in string1:
        if i not in hash_:
            hash_[i] = 1
        elif i in hash_:
            hash_[i] +=1
    for j in string2:
        if j not in hash_:
            return False
        elif j in hash_:
            if hash_[j] == 0:
                return False
            hash_[j] -= 1
    return sum(list(hash_.values())) == 0

print(is_perm('hey','hey'))
print(is_perm("yeh",'yhe'))
print(is_perm("Boom","Boo"))