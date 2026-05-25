import pandas as pd

a=int(input("Enter the number of students: "))
stdata={}
idlist=[]
namelist=[]
moblist=[]
emaillist=[]
    
for i in range(a):
    print("The Info of Student ",i+1)
    id=int(input("Enter the student id: "))
    name=input("Enter the student name: ")
    mob=input("Enter the mobile number: ")
    email=input("Enter the email id: ")
    idlist.append(id)
    namelist.append(name)
    moblist.append(mob)
    emaillist.append(email)

stdata['Id']=idlist
stdata['Name']=namelist
stdata['Mobile']=moblist
stdata['Email']=emaillist
print(stdata)

student=pd.DataFrame(stdata)
print(student)



id_search=int(input("Enter the Id to be searched: "))

if id_search in stdata['Id']:
    stinfo=student[student['Id']==id_search]
    print(stinfo)
else:
    print("The Id does not exit")


