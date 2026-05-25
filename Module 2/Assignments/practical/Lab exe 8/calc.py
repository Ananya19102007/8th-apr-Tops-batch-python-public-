def getsum(a,b):
    sum=a+b
    print(sum)

def getsub(a,b):
    sub=a-b
    print(sub)

def getmul(a,b):
    mul=a*b
    print(mul)

def getdiv(a,b):
    div=a/b
    print(div)

a=int(input("Enter number A: "))
b=int(input("Enter number A: "))
ch=input("Enter ur choice (add,sub,mul,div): ")

if ch=="add":
    getsum(a,b)
elif ch=="sub":
    getsub(a,b)
elif ch=="mul":
    getmul(a,b)
elif ch=="div":
    getdiv(a,b)
else:
    print("WRONG CHOICE!")