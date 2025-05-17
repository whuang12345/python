from student import Student
from student import Course

# Example usage
student1 = Student("Alice", 20, "S12345")
course1 = Course("Mathematics", "MATH101")
course2 = Course("Physics", "PHYS101")

student1.enroll(course1)
student1.enroll(course2)

student1.display_courses()

x = input("Enter a number: ")
y = 10 + int(x)

# This is a test for the Student and Course classes.
print(f"You entered: {x} and math.plus 10 is: {y}")