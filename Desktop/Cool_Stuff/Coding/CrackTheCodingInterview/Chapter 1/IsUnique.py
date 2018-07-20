def is_Unique(string):
    hash_ = {}
    for i in string:
        if i not in hash_:
            hash_[i] = 1
        elif i in hash_:
            return False
    return True

print(is_Unique("hey"))
print(is_Unique("BOOM"))
