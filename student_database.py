# Write your solution here
def add_student(students: dict, student_name: str):
    students[student_name] = ()

def print_student(students: dict, student_name: str):
    
    if student_name not in students:
        print(f"{student_name}: no such person in the database")
    else:
        if len(students[student_name]) == 0:
            x = " no completed courses"
        else:
            x = f" {(len(students[student_name]))} completed courses:" 
        print(f"{student_name}:")
        print(  x)
        for index in range(len(students[student_name])):
            print(f"  {students[student_name][index][0]} {students[student_name][index][1]}")
        if x != " no completed courses":
            total_grade = 0
            for course in students[student_name]:
                total_grade += course[1]
            average_grade = total_grade / len(students[student_name])
            print(f" average grade {average_grade}")

def add_course(students: dict, student_name: str, course: tuple):
    course_taken = False
    if course[1] == 0:
        return 
    if students[student_name] == ():
        students[student_name] = []
        students[student_name].append(course)
    for course_index in range(len(students[student_name])):
        if course[0] in students[student_name][course_index]:
            course_taken = True
            if course[1] <= students[student_name][course_index][1]:
                return
            else:
                students[student_name].remove(students[student_name][course_index])
                students[student_name].append(course)
    if course_taken == False:
        students[student_name].append(course)


def summary(students: dict):
    num_of_students = len(students)
    num_of_courses = []
    for student in students:
        num_of_courses.append(len(students[student]))
    most_course_num = max(num_of_courses)
    course_student_index = num_of_courses.index(most_course_num)
    list_of_students = list(students)
    most_course_student = list_of_students[course_student_index]
    grade = []
    total_grade = 0
    for student in students:
        for course in students[student]:
            total_grade += course[1]
        average_grade = total_grade / len(students[student])
        grade.append(average_grade)
        total_grade = 0
    best_grade = max(grade)
    grade_student_index = grade.index(best_grade)
    best_grade_student = list_of_students[grade_student_index]
    print(f"students {num_of_students}")
    print(f"most courses completed {most_course_num} {most_course_student}")
    print(f"best average grade {best_grade} {best_grade_student}")




