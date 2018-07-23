o = open("output.txt","a") #open for append
for line in open("template.txt"):
    line = line.replace("xx","100").replace("yy","200")
    o.write(line + "\n") 
o.close()
