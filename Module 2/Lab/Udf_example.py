def getdata(id,name,city):
    print("ID:-",id)
    print("Name:-",name)
    print("City:-",city)

"""a=input("Id: ")
b=input("Name: ")
c=input("City: ")

getdata(a,b,c)"""

x=int(input("Enter the number of students: "))

for i in range(x):
    a=input("Id: ")
    b=input("Name: ")
    c=input("City: ")
    print("Details of student ",i+1)
    getdata(id=a,name=b,city=c)

