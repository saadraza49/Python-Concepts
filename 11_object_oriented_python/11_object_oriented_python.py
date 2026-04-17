class Student:
    """Student class demonstrating OOP basics."""

    def __init__(self, name, age, grade):
        self.__name  = name   # Encapsulation (private)
        self.__age   = age
        self.__grade = grade

    # Getters
    def get_name(self):  return self.__name
    def get_age(self):   return self.__age
    def get_grade(self): return self.__grade

    # Setter
    def set_grade(self, grade):
        self.__grade = grade

    def display_info(self):
        print(f"  Student → Name: {self.__name}, Age: {self.__age}, Grade: {self.__grade}")


class Teacher(Student):
    """Teacher class inheriting Student."""

    def __init__(self, name, age, grade, subject):
        super().__init__(name, age, grade)
        self.__subject = subject

    def display_info(self):
        print(f"  Teacher → Name: {self.get_name()}, Age: {self.get_age()}, "
              f"Grade: {self.get_grade()}, Subject: {self.__subject}")

    def teach(self):
        print(f"  {self.get_name()} is teaching {self.__subject}.")


# Create objects
s1 = Student("Ayesha", 18, "A")
s2 = Student("Bilal",  20, "B")

print("Student Objects:")
s1.display_info()
s2.display_info()

# Update grade via setter
s2.set_grade("A")
print("After grade update:")
s2.display_info()

# Teacher (inheritance)
t1 = Teacher("Mr. Hassan", 35, "PhD", "Python Programming")
print("\nTeacher Object (Inheritance):")
t1.display_info()
t1.teach()
