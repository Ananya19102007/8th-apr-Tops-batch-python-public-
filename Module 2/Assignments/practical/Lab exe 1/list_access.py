data=[]
a=int(input("Enter the number of elements: "))

for i in range(a):
    ele=input("Enter the elements : ")
    data.append(ele)

print(data)

x=input("Enter the element to be searched: ")

if x in data:
    print(data.index(x))
else: 
    print("element doesnt exist!")
