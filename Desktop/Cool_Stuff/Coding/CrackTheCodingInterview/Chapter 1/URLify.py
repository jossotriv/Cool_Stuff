def URLify(string,length):
    string_=[]
    for i in range(length):
        if string[i] == " ":
            string_.append("%20")
        else:
            string_.append(string[i])
    return "".join(string_)

if '__main__' == __name__:
    print(URLify('hey ',4))
    print(URLify("Hey my name is Joel, the buider.     ",len("Hey my name is Joel, the buider.     ")))
