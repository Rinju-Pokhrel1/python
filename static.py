# Implementation of constructor, instance method, and static method

class student:
    college_name = "Padma Kanya College"  # class attribute
    name = "Unknown"                      # class attribute

    def __init__(self, fulname, address):
        self.name = fulname              # object attribute
        self.address = address           # object attribute

    def welcome(self):                   # instance method
        print("Welcome all,", self.name)

    @staticmethod
    def hello():                         # static method
        print("Hello")

# Creating objects
s1 = student("Rinju Pokhrel", "Kathmandu")
print(s1.name)       # object attribute
print(s1.address)
s1.welcome()         # instance method
s1.hello()           # static method (can also call using class name)

s2 = student("Sitara", "Lalitpur")
print(s2.name)
print(s2.address)
s2.welcome()
s2.hello()
