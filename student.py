class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display_courses(self):
        if self.courses:
            print(f"{self.name} is enrolled in the following courses:")
            for course in self.courses:
                print(f"- {course.course_name} ({course.course_code})")
        else:
            print(f"{self.name} is not enrolled in any courses.")

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

