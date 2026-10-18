class student:
    grade = 10
    name= "Erwan"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("my name is ",self.name)
        print("I study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()
