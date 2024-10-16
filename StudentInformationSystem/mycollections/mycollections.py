class Student:
    def _init_(self, student_id, first_name, last_name, dob, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_number = phone_number
        self.enrollments = []  # List to hold enrollment objects

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)


class Course:
    def _init_(self, course_id, course_name="", course_code="", instructor_name=""):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = []  # List to hold enrollments

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)


class Enrollment:
    def _init_(self, enrollment_id, student_id, course_id, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date
        # Adding this enrollment to student and course upon creation
        student_id.add_enrollment(self)
        course_id.add_enrollment(self)


class Teacher:
    def _init_(self, teacher_id, first_name="", last_name="", email=""):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []  # List of courses assigned to this teacher

    def assign_course(self, course):
        self.assigned_courses.append(course)
        course.teacher = self


class Payment:
    def _init_(self, payment_id, student_id, amount, payment_date):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date