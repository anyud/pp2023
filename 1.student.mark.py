def input_students():
    n = int(input("Enter the number of students in the class: "))
    students = []
    for i in range(n):
        id = input(f"Enter the id for student {i+1}: ")
        name = input(f"Enter the name for student {i+1}: ")
        dob = input(f"Enter the date of birth for student {i+1} : ")
        students.append((id, name, dob))
    return students

def input_courses():
    n = int(input("Enter the number of courses: "))
    courses = []
    for i in range(n):
        id = input(f"Enter the id for course {i+1}: ")
        name = input(f"Enter the name for course {i+1}: ")
        courses.append((id, name))
    return courses

def input_marks(students, courses):
    course_id = input("Enter the id of the course: ")
    while course_id not in [c[0] for c in courses]:
        print("Invalid course id. Please try again.")
        course_id = input("Enter the id of the course: ")
    marks = []
    for student in students:
        mark = input(f"Enter the mark for student {student[1]} in course {course_id}: ")
        marks.append((student[0], mark))
    return (course_id, marks)

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"- {course[0]}: {course[1]}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"- {student[0]}: {student[1]}")

def show_marks(course_id, students, marks):
    print(f"Marks for course {course_id}:")
    for mark in marks:
        student_name = [s[1] for s in students if s[0] == mark[0]][0]
        print(f"- {student_name}: {mark[1]}")

students = input_students()
courses = input_courses()

while True:
    print("\nMenu:")
    print("1. Input marks")
    print("2. List courses")
    print("3. List students")
    print("4. Show marks for a course")

    choice = input("Enter your choice: ")
    if choice == "1":
        marks = input_marks(students, courses)
    elif choice == "2":
        list_courses(courses)
    elif choice == "3":
        list_students(students)
    elif choice == "4":
        if 'marks' not in locals():
            print("Please input marks first.")
        else:
            show_marks(marks[0], students, marks[1])
        break
    else:
        print("Invalid choice. Please try again.")