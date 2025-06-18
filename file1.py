f=open("file.txt","r")
data =f.read(5)

print(data)
data=f.readline()
print(data)

print(type(data))
f.close()
