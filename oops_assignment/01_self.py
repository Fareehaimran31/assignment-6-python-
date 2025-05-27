class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age
    def display(self):
        print(f"Name:{self.name},Marks:{self.marks}")
s1 = Student("Mus'haf", 85)
s1.display()