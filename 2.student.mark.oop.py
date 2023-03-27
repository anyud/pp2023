class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        n = int(input("Enter the number of students in the class: "))
        for i in range(n):
            id = input(f"Enter the id for student {i+1}: ")
            name = input(f"Enter the name for student {i+1}: ")
            dob = input(f"Enter the date of birth for student {i+1} : ")
            student = Student(id, name, dob)
            self.students.append(student)

    def input_courses(self):
        n = int(input("Enter the number of courses: "))
        for i in range(n):
            id = input(f"Enter the id for course {i+1}: ")
            name = input(f"Enter the name for course {i+1}: ")
            course = Course(id, name)
            self.courses.append(course)

    def input_marks(self):
        course_id = input("Enter the id of the course: ")
        while course_id not in [c.id for c in self.courses]:
            print("Invalid course id. Please try again.")
            course_id = input("Enter the id of the course: ")
        for student in self.students:
            mark = input(f"Enter the mark for student {student.name} in course {course_id}: ")
            mark = Mark(student, course_id, mark)
            self.marks.append(mark)

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"- {course.id}: {course.name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"- {student.id}: {student.name}")

    def show_marks(self):
        course_id = input("Enter the id of the course: ")
        marks = [m for m in self.marks if m.course == course_id]
        print(f"Marks for course {course_id}:")
        for mark in marks:
            student_name = mark.student.name
            print(f"- {student_name}: {mark.mark}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Input marks")
            print("2. List courses")
            print("3. List students")
            print("4. Show marks for a course")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.input_marks()
            elif choice == "2":
                self.list_courses()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.show_marks()
                break
            else:
                print("Invalid choice. Please try again.")

school = School()
school.input_students()
school.input_courses()
school.menu()
