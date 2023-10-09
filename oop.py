class People():
    def __init__(self, name, age):
        print("Called constructor")
        self.name = name
        self.age = age
        self.__password = None

    def login_your_account(self):
        #send_request self.name and self.__password
        print(self.__password)

    def _dance(self):
        print("Dancing...")

    def speak(self):
        print("Speaking...")
        # print("My name is: ", self.get_personal_information())

    def read(self):
        print("Reading...")

    def learn(self):
        print("Learning...")

    def get_personal_information(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")


class Student(People):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
        self.univercity = None

    def get_personal_information(self):
        super().get_personal_information()
        print(f"ID is: {self.id}")

    def set_university_name(self, university):
        self.univercity = university

    def get_university_name(self):
        return self.univercity


student1 = Student("John", 33, 1)
student1.get_personal_information()


person1 = People("Jesica", 22)
# print(person1.__password)
person1.dance()
# person1.password = "PythonTraining2023"