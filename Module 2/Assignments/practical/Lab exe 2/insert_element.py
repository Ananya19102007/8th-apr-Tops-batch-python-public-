data=[]
a=int(input("Enter the number of elements: "))

for i in range(a):
    ele=input("Enter the elements : ")
    data.append(ele)

print(data)

ele2=input("Enter the element to be inserted: ")
pos=input("Enter the position of the element: ")
data=data.insert(pos,ele2)
print(data)