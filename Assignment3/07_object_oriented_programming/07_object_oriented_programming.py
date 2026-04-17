# ============================================================
# PART 7 – Object-Oriented Programming  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 7 – Object-Oriented Programming (OOP)")
print("=" * 60)

# Base class with encapsulation
class Person:
    def __init__(self, name, age):
        self._name = name   # protected
        self._age  = age

    def display(self):
        print(f"  Name: {self._name}, Age: {self._age}")

    def __str__(self):
        return f"Person({self._name}, {self._age})"


class Student(Person):
    def __init__(self, name, age, grade, marks):
        super().__init__(name, age)
        self.__grade = grade    # private (encapsulation)
        self.__marks = marks

    def get_grade(self):  return self.__grade
    def get_marks(self):  return self.__marks
    def set_grade(self, g): self.__grade = g

    def display(self):   # polymorphism (override)
        print(f"  [Student] Name: {self._name}, Age: {self._age}, "
              f"Grade: {self.__grade}, Marks: {self.__marks}")

    def study(self):
        print(f"  {self._name} is studying hard!")


class Teacher(Person):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.__subject    = subject
        self.__experience = experience

    def display(self):   # polymorphism (override)
        print(f"  [Teacher] Name: {self._name}, Age: {self._age}, "
              f"Subject: {self.__subject}, Exp: {self.__experience} yrs")

    def teach(self):
        print(f"  {self._name} is teaching {self.__subject}.")


# Objects
s1 = Student("Ayesha", 18, "A+", 95)
s2 = Student("Bilal",  20, "B",  74)
t1 = Teacher("Mr. Akbar", 38, "Python", 10)
t2 = Teacher("Ms. Hina",  32, "Data Science", 7)

print("Student Objects:")
s1.display()
s2.display()
s1.study()

print("\nTeacher Objects:")
t1.display()
t2.display()
t1.teach()

# Polymorphism demo
print("\nPolymorphism – calling display() on mixed list:")
people = [s1, s2, t1, t2]
for p in people:
    p.display()

# Update via setter
print("\nEncapsulation – update Bilal's grade:")
s2.set_grade("A")
s2.display()

# Additional class: Shape polymorphism
class Shape:
    def area(self): return 0

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self):
        import math
        return round(math.pi * self.r**2, 2)

class Rectangle(Shape):
    def __init__(self, w, h): self.w = w; self.h = h
    def area(self): return self.w * self.h

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
print("\nShape Polymorphism:")
for sh in shapes:
    print(f"  {sh.__class__.__name__} area = {sh.area()}")
