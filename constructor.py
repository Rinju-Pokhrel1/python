# Implementation of constructor

class student:
    college_name = "Padma Kanya College"
    name = "Unknown" #class attr

    def __init__(self, fulname, address):
        self.name = fulname #object attr
        self.address = address

print("Adding new student to the database")

# Corrected with both name and address
s1 = student("Rinju Pokhrel", "Kathmandu")
print(s1.name)
print(s1.address)

s2 = student("Sitara", "Lalitpur")
print(s2.name)
print(s2.address)
 ##output:object attr>class atr
