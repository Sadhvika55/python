n=int(input("enter the number:"))
a=0
b=1
sums=0
count=1
while(n>count):
    sums=a+b
    print(sums)
    a=b
    b=sums
    count+=1

