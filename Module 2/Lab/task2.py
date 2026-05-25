import random as rn
import datetime as dt

a=int(input("Enter the number of Students: "))

for i in range(a):
    print("------------------------------")
    print("Enter the Data of Student ",i+1)
    cr=dt.datetime.now()
    id=rn.randint(100,999)
    name=input("Enter the name of the student: ")
    city=input("Enter the name of the city: ")

    print("==========================")
    print("The data of Student ",i+1," is as follows:")
    print(cr)
    print(id)
    print(name)
    print(city)
