"""stdata=[
    {'id':101,'Name':'Ananya','City':'Rajkot'},
    {'id':102,'Name':'Suhani','City':'Surat'},
    {'id':103,'Name':'Isha','City':'Rajkot'},
    {'id':104,'Name':'Jeeya','City':'Surat'},
    {'id':105,'Name':'Preesha','City':'Rajkot'},
]
print(stdata)"""


stlist=[]
stdata={}
a=int(input("Enter the Number of Students: "))
b=int(input("Enter the number of elements: "))

for i in range(a):
    for j in range(b):
        key=input("Enter the key:")
        value=input("Enter the Value:")
        stdata[key]=value
        stlist.append(stdata)
    
print(stlist)

