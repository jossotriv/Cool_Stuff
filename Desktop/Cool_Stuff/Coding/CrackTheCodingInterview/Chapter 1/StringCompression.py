import string as st
def compressor(string):
    hash_ = {}
    new_string = []
    for i in string:
        if i not in hash_:
            hash_[i] = 1
        elif i in hash_:
            hash_[i] +=1
    for j in hash_:
        new_string.append(j + str(hash_[j]))
    new_string= "".join(new_string)
    if len(new_string) > len(string):
        return string
    else:
        return new_string

print("Test Case #1:")

print(compressor('hello'))

print("Test Case # 2:")

print(compressor('collaboration'))

print("Test Case # 3:")
print(compressor('aaaaaabbbbaaa'))
