file=open('Student.txt','a')

a=int(input("Enter the number of students: "))

for i in range(a):
    id=input("Enter the id: ")
    name=input("Enter the name: ")
    file.write("\nID:")
    file.write(id)
    file.write("\nName:")
    file.write(name)
    file.write("\n-------------------------------")
