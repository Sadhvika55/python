f1=open("step1.txt","r")
content=" "
for i in f1:
    content=content+i
f1.close()
f2=open("cpystep1.txt","w")
f2.write(content)
f2.close()
f2=open("cpystep1.txt","r")
print(f2.read())

