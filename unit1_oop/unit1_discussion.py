"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented
programming (OOP) concepts in Python.
"""

from copy import copy, deepcopy


# TODO 1:
# Parent class
class ParentClass:

    # class variable shared by all objects
    category = "Person"

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# TODO 2:
# Child class inherits from ParentClass
class ChildClass(ParentClass):

    # new class variable
    school_name = "UMGC"

    def __init__(self, name, age, student_id, major):
        # call the parent constructor
        super().__init__(name, age)

        # new instance variables
        self.student_id = student_id
        self.major = major
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    # override the parent display_info method
    def display_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Student ID: {self.student_id}, Major: {self.major}"
        )

    # Student-created extension
    def course_count(self):
        return len(self.courses)


# TODO 3:
# Demonstrate class and instance namespaces
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass(
        "Alex",
        21,
        "S101",
        "Computer Science"
    )

    student2 = ChildClass(
        "Jordan",
        23,
        "S102",
        "Cybersecurity"
    )

    # access class variable through the class
    print("School through class:", ChildClass.school_name)

    # access the same class variable through an object
    print("School through student1:", student1.school_name)

    # add an attribute to only student1
    student1.nickname = "AJ"

    print("\nStudent 1 namespace:")
    print(student1.__dict__)

    print("\nStudent 2 namespace:")
    print(student2.__dict__)

    print("\nChild class namespace:")
    print(ChildClass.__dict__.keys())


# TODO 4:
# Demonstrate shallow and deep copying
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Taylor",
        22,
        "S103",
        "Computer Science"
    )

    # courses is mutable data stored inside the object
    original.add_course("CMSC 315")
    original.add_course("CMSC 220")

    # shallow copy shares nested mutable objects
    shallow_copy = copy(original)

    # deep copy creates its own copy of nested data
    deep_copy = deepcopy(original)

    print("\nBefore changing the original:")
    print("Original courses:", original.courses)
    print("Shallow copy courses:", shallow_copy.courses)
    print("Deep copy courses:", deep_copy.courses)

    # change the nested list in the original object
    original.courses.append("CMSC 320")

    print("\nAfter adding CMSC 320 to the original:")
    print("Original courses:", original.courses)
    print("Shallow copy courses:", shallow_copy.courses)
    print("Deep copy courses:", deep_copy.courses)

    print(
        "\nThe shallow copy changed because it shares the same "
        "course list with the original."
    )

    print(
        "The deep copy did not change because it has its own "
        "separate copy of the list."
    )


# TODO 5:
# Main function
def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")

    parent = ParentClass("Chris", 30)
    print(parent.display_info())
    print("Category:", ParentClass.category)

    print("\n=== Child Object ===")

    student = ChildClass(
        "Sam",
        20,
        "S100",
        "Computer Science"
    )

    student.add_course("CMSC 315")
    student.add_course("CMSC 220")

    # overridden method from the child class
    print(student.display_info())

    print("School:", student.school_name)
    print("Courses:", student.courses)

    # student-created extension
    print("Number of courses:", student.course_count())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()