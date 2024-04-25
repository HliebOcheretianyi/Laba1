"""
NaUKMA

Faculty1            Faculty2            Faculty3
kaf11    kaf12      kaf21  Kaf22        kaf31  Kaf32
groups
student + teachers
"""


class University:
    allKafedras = []
    allGroups = []
    allTeachers = []
    allStudents = []

    """
    Вивести інформацію про всіх студентів впорядкованих за курсами.
    Вивести інформацію про всіх студентів/викладачів факультета впорядкованих за алфавітом.
    Вивести інформацію про всіх студентів кафедри впорядкованих за курсами.
    Вивести інформацію про всіх студентів/викладачів кафедри впорядкованих за алфавітом.
    Вивести інформацію про всіх студентів кафедри вказаного курсу.
    Вивести інформацію про всіх студентів кафедри вказаного курсу впорядкованих за алфавітом.
    """
    def get_students_by_course(self, course):  # doesnt work
        course_students = [
            student for student in University.allStudents if student.course == course
        ]
        return course_students



class Faculty:


    def __init__(self, name: str):
        self.name = name
        self.kafedras = []

    def rename(self, new_name):
        self.name = new_name

    def add_kafedra(self, kafedra):
        try:
            if isinstance(kafedra, Kafedra):
                if kafedra not in self.kafedras:
                    self.kafedras.append(kafedra)
                    University.allKafedras.append(kafedra)
                else:
                    raise ValueError("Kafedra already exists in the list.")
            else:
                raise ValueError("Invalid kafedra object. Expected instance of Kafedra class.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def remove_kafedra(self, kafedra):
        try:
            if isinstance(kafedra, Kafedra):
                if kafedra in self.kafedras:
                    self.kafedras.remove(kafedra)
                    University.allKafedras.remove(kafedra)
                else:
                    raise ValueError("Kafedra is not yet assigned")
            else:
                raise ValueError("Invalid kafedra object. Expected instance of Kafedra class.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def get_info(self):
        info = f"Faculty Name: {self.name}\n"
        info += "Kafedras:\n"
        for kafedra in self.kafedras:
            info += f"  - {kafedra.name}\n"
        return info


class Kafedra:


    def __init__(self, name: str, faculty: Faculty):
        self.name = name
        self.faculty = faculty
        self.groups = []
        self.teachers = []

    def rename(self, new_name):
        self.name = new_name

    def rearange(self, new_faculty):
        self.faculty = new_faculty

    def add_group(self, group):
        try:
            if isinstance(group, Group):
                if group not in self.groups:
                    self.groups.append(group)
                    University.allGroups.append(group)
                else:
                    raise ValueError("Group already exists in the list.")
            else:
                raise ValueError("Invalid Group object. Expected instance of Group class.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def remove_group(self, group):
        try:
            if group in self.groups:
                self.groups.remove(group)
                University.allGroups.remove(group)
            else:
                raise ValueError("Group is not yet assigned")
        except ValueError as ve:
            print(f"Error: {ve}")

    def add_teacher(self, teacher):
        try:
            if isinstance(teacher, Teacher):
                if teacher not in self.teachers:
                    self.teachers.append(teacher)
                    University.allTeachers.append(teacher)
                else:
                    raise ValueError("Teacher already exists in the list.")
            else:
                raise ValueError("Invalid Teacher object. Expected instance of Teacher class.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def remove_teacher(self, teacher):
        try:
            self.teachers.remove(teacher)
            University.allTeachers.remove(teacher)
        except ValueError as ve:
            print(f"Error: {ve}")


class Group:


    def __init__(self, number: int, kafedra: Kafedra):
        self.number = number
        if not isinstance(kafedra, Kafedra):
            raise ValueError("Invalid kafedra object. Expected instance of Kafedra class.")
        self.kafedra = kafedra
        self.students = []

    def add_student(self, student):
        try:
            if isinstance(student, Student):
                if student not in self.students:
                    self.students.append(student)
                    University.allStudents.append(student)
                else:
                    raise ValueError("Student already exists in the list.")
            else:
                raise ValueError("Invalid Student object. Expected instance of Student class.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def remove_student(self, student):
        try:
            self.students.remove(student)
            University.allStudents.remove(student)
        except ValueError as ve:
            print(f"Error: {ve}")

    def get_info(self):
        info = f"Group Number: {self.number}\n"
        info += f"Kafedra: {self.kafedra.name}\n"
        info += "Students:\n"
        for student in self.students:
            info += f"  - {student.name} {student.surname}\n"
        return info


class Student:
    def __init__(self, name: str, surname: str, kafedra: Kafedra, course: int, group: Group):
        self.name = name
        self.surname = surname
        self.kafedra = kafedra
        self.course = course
        self.group = group


class Teacher:
    def __init__(self, name: str, surname: str, kafedra: Kafedra):
        self.name = name
        self.surname = surname
        self.kafedra = kafedra


if __name__ == "__main__":
    FI = Faculty("FI")
    math = Kafedra("Math", FI)

    faculty = Faculty("Test Faculty")
    for i in range(6):
        kafedra = Kafedra(f"Kafedra {i}", faculty)
        faculty.add_kafedra(kafedra)

    for i in range(6):
        kafedra = Kafedra(f"Kafedra na FI {i}", FI)
        FI.add_kafedra(kafedra)

    print(FI.get_info())
    print(faculty.get_info())
    faculty = Faculty("Engineering")
    department = Kafedra("Computer Science", faculty)
    group1 = Group(1, department)
    group2 = Group(2, department)
    student1 = Student("John", "Doe", department, 1, group1)
    student2 = Student("Jane", "Smith", department, 2, group2)
    student3 = Student("Mike", "Johnson", department, 1, group1)

    university = University()
    course_students = university.get_students_by_course(1)
    print(course_students)
