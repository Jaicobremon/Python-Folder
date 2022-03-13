class Car(object):
    def __init__(self, model, color ,company, speedlimit):
        self.color = color
        self.company = company
        self.speedlimit = speedlimit
        self.model = model
    
    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def change_gear(self,gear_type):
        print("Gear changed")

Mercedes = Car("421","Red","Mercedes","100")

print(Mercedes.color)

print(Mercedes.change_gear(4))

class Student(object):
    def __init__(self,marks,student_number,grade,gender,age):
        self.marks = marks
        self.student_number = student_number
        self.grade = grade
        self.gender = gender
        self.age = age
    
    def goToSchool(self):
        print("Get Started")

    def goodStudent(self,grade):
        if grade >= 91:
            print("Your a good student")
        else:
            print("Work harder")

Student1 = Student("91","735","9","Male","15")

print(Student1.marks)

print(Student1.goToSchool())

print(Student1.goodStudent(91))


