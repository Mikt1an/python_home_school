import datetime

class Student:
    MIN_AGE = 16
    id = 1
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        self.student_id = Student.id
        Student.id += 1
        if self.age() < Student.MIN_AGE:
            raise ValueError("user must be > 16")

    def age(self):
        now = datetime.datetime.now()
        age_student = now.year - self.date_of_birth.year
        if (now.month, now.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age_student -= 1
        return age_student

    @staticmethod
    def student_age(age):
        age = datetime.datetime.strptime(age, "%Y-%m-%d").date()
        now = datetime.datetime.now()
        age_student = now.year - age.year
        if (now.month, now.day) < (age.month, age.day):
            age_student -= 1
        return age_student

    def __str__(self):
        return f"Student: {self.name}, birth_date: {self.date_of_birth}, ID: {self.student_id}"

    def student_info(self):
        return f"Student:\n\tName: {self.name}\n\tAge: {self.age()}\n\tID: {self.student_id}"

    @classmethod
    def alter_constr(cls, text):
        name, date_of_birth= text.split(",")
        name = name.strip()
        date_of_birth = date_of_birth.strip()
        return cls(name, date_of_birth)

    def age_to_date(self, date):
        now = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        age_date = now.year - self.date_of_birth.year
        if (now.month, now.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age_date -= 1
        return age_date










st1 = Student.alter_constr("Anton, 2000-01-01")
print(st1, f"\n", st1.student_info())
print(st1.age_to_date("2000-01-01"))

# print(Student.student_age("2019-01-01"))
# try:
#     st1 = Student("Anton", "2000-01-01")
#     print(st1)
#     print(st1.student_info())
#     print(st1.alter_constr())
# except ValueError as e:
#     print(e)
