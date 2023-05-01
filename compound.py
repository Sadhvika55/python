def compoundinterest(p,r,t):
    ci=p*(pow((1+r/100),t))
    return ci
p=float(input("enter the amount"))
r=float(input("enter the interest :"))
t=float(input("enter the years:"))
ci=compoundinterest(p,r,t)
print("compound interest:{}".format(ci))


