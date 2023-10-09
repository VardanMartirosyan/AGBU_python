class People():
    name = None
    age = None

    def __init__(self, name, age):
        print("Called constructor")
        self.name = name
        self.age = age

    def dance(self):
        print("Dancing...")

    def speak(self):
        print("Speaking...")
        print("My name is: ", self.get_personal_information())

    def get_personal_information(self):
        return self.name

    def read(self):
        print("Reading...")

    def get_age(self):
        return self.age


person1 = People("John", 33)
person2 = People("Jesica", 22)

print(person1.name)
print(person2.name)
# print(type(person1))
# person1.name = "John"
# person1.age = 33
#
# person1.dance()
# person1.speak()
# print(person1.get_age())
#
#
#
#
#
#


