stdata={'id':101,'name':'ananya','city':'rajkot'}

print(stdata)
print(stdata['name'])
print(stdata.get('city'))
print(stdata.keys())
print(stdata.values())
print(len(stdata))

if 'name' in stdata:
    print("yess")
else:
    print("no")
