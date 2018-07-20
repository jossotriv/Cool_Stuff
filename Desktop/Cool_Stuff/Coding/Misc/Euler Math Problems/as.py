def sub_lists(my_list):
    subs = [[]]
    max_ = 0
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            subs.append(sub)
            n += 1
    for l in range(len(subs)):
            if len(subs[l]) > max_:
                max_ = len(subs[l])
    return subs
    

l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print(sub_lists(l1))
print(sub_lists(l2))
