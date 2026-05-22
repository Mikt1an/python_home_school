# 1

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    def __init__(self, name, num_course):
        super().__init__(name)
        self.num_course = num_course

    def introduce(self):
        super().introduce()
        print(f"I am on course {self.num_course}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}. \nMy subject is {self.subject}.")



title = [
    Student("Anthony", 4),
    Teacher("Olha", "Mathematics"),
]
for person in title:
    person.introduce()
    print("-" * 50)
