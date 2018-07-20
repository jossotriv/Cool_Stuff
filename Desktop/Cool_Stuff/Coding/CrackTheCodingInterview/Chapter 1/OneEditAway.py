def is_it_doable(string_1,string_2):
    edit = 0
    if string_1 == string_2 or abs(len(string_1) - len(string_2)) == 1:
        return True
    elif abs(len(string_1) - len(string_2)) > 1:
        return False
    else:
        i_1 = 0
        i_2 = 0
        while len(string_1) != 0 or len(string_2) != 0:
            if string_1[i_1] == string_2[i_2]:
                string_1 = string_1[i_1:len(string_1)]
                string_2 = string_2[i_2:len(string_2)]
                i_1 +=1
                i_2 +=1
            elif string_1[i_1] != string_2[i_2]:
                if string_1[i_1+1] == string_2[i_2]:
                    i_1 +=1
                    edit +=1
                elif string_1[i_1] ==string_2[i_2 +1]:
                    i_2 += 1
                    edit +=1
                else:
                    return False
    return edit <=1
print("Test Case 1- Identitical:")
print(is_it_doable('hey','hey'))
print("Test Case 2- Insertion of 1")
print(is_it_doable('h',''))
print("Test Case 3- Difference greater than 1 length")
print(is_it_doable('he',''))
print("Test Case 4- Random Check")
print(is_it_doable('hola','hola'))
print("Test Case 5- Broke")
print(is_it_doable('pale','bake'))
