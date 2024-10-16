from mycollections.mycollections import *
from customexceptions.myexception import *
from mycollections.mycollections import Student
from util.DBConnection import DBConnection


class StudentInformationImpl():
    def __init__(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()

    def create_student(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
           self.firstName = input("Enter student first name: ")
           self.lastName = input("Enter student last name: ")
           self.dateOfBirth = input("Enter student date of birth: ")
           self.email = input("Enter student email id: ")
           self.phoneNumber = input("Enter student phone number: ")
           cursor.execute(
            "INSERT INTO Student (firstName, lastName, dateOfBirth, email, phoneNumber) "
            "VALUES (?,?,?,?,?)",
            (self.firstName, self.lastName, self.dateOfBirth, self.email, self.phoneNumber))
           print("Student created successfully")
           conn.commit()
           conn.close()
        except InvalidStudentDataException as e:
           print(e)
        except Exception as e:
            (print(str(e) + "---Error in creating student:---"))
        return None

    def create_course(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            self.courseName= input("Enter course_name: ")
            self.courseCode = input("Enter course_code ")
            self.teacherId = int(input("Enter teacher id: "))
            cursor.execute(
            "INSERT INTO Course (courseName, courseCode, teacherId) VALUES (?,?,?)",
            (self.courseName, self.courseCode, self.teacherId))
            print("Course created successfully")
            conn.commit()
            conn.close()

        except InvalidCourseDataException as e:
                print(e)

        except Exception as e:
                (print(str(e) + "---error in creating course:---"))


    def create_enrollment(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            self.student_id= int(input("Enter student_id: "))
            self.course_id= int(input("Enter course_id "))
            self.enrollment_date = input("Enter enrollment_date: ")
            cursor.execute(
                "INSERT INTO Enrollment (studentId, courseId, enrollmentDate) VALUES (?,?,?)",
                (self.student_id, self.course_id,self.enrollment_date))
            print("Enrollment created successfully")
            conn.commit()
            conn.close()
        except InvalidEnrollmentDataException as e:
           print(e)
        except Exception as e:
            (print(str(e) + "---error in creating enrollment:---"))

    def create_teacher(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            self.firstName = input("Enter first_name: ")
            self.lastName = input("Enter last_name ")
            self.email = input("Enter email: ")

            cursor.execute(
                "INSERT INTO Teacher (firstName, lastName, email) VALUES (?,?,?)",
                (self.firstName, self.lastName, self.email))
            print("New Teacher has been created")

            conn.commit()
        except InvalidTeacherDataException as e:
           print(e)
        except Exception as e:
            (print(str(e) + "---error in creating teacher:---"))
        conn.close()
        return None

    def create_payment(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            self.studentId = int(input("Enter student_id: "))
            self.amount = int(input("Enter amount "))
            self.paymentDate = input("Enter payment_date: ")

            cursor.execute("INSERT INTO Payment (studentId, amount, paymentDate) VALUES (?,?,?)",
                           (self.studentId, self.amount,self.paymentDate))
            print("New Payment has been created")

            conn.commit()
            conn.close()
        except InsufficientFundsException as e:
            print(e)


    def get_student_by_id(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            self.studentId = int(input("Enter student_id: "))
            cursor.execute("SELECT * FROM Student WHERE studentId = ?", (self.studentId,))
            student = [list(row) for row in cursor.fetchall()]
            if student:
                print(student)
            else:
                raise StudentNotFoundException("entered student_id is not found")
        except StudentNotFoundException as e:
                print(e)
        except Exception as e:(
                print(str(e) + "---error in getting students:---"))

    def get_course_by_id(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            self.courseId = int(input("Enter course_id: "))
            cursor.execute("SELECT * FROM Course WHERE courseId = ?",[(self.courseId)])
            row = cursor.fetchone()

            if row:
                course = Course(row[0], row[1], row[2], row[3])
                conn.close()
                print(course)
            else:
                raise CourseNotFoundException("entered course_id is not found")
        except CourseNotFoundException as e:
                print(e)


    def get_enrollments_for_student(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student_id: "))
            cursor.execute("SELECT * FROM Enrollment WHERE studentId = ?", [(self.student_id)])
            rows = cursor.fetchall()

            enrollments = []
            for row in rows:
                course = StudentInformationImpl.get_course_by_id(row[2])
                enrollment = Enrollment(row[0], Student, course, row[3])
                enrollments.append(enrollment)

                conn.close()
                print(enrollments)
        except InvalidEnrollmentDataException as e:
            print(e)

    def get_enrollments_for_course(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.courseName = input("Enter courseName: ")
            cursor.execute(" SELECT s.firstName, s.lastName, e.enrollmentDate FROM Enrollment e JOIN Student s ON e.studentId = s.studentId Join Course c on e.courseId=c.courseId WHERE courseName = ?",(self.courseName,))
            rows = cursor.fetchall()
            print(rows)

            return rows

        except InvalidEnrollmentDataException as e:
            print(e)

    def generate_report(self,courseName):
        courseName = input("Enter courseName: ")
        enrollments = self.get_enrollments_for_course(courseName)
        report = f"Enrollment Report for {courseName}:\n"
        for enrollment in enrollments:
            report += f"{enrollment[0]} {enrollment[1]} - {enrollment[2]}\n"
        print(report)

    def enroll_in_course(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.student_id=int(input("enter student_id:"))
            self.course_id=int(input("course_id:"))
            self.enrollment_date=input("enter enrollment_date: ")
            cursor.execute( "INSERT into Enrollment (studentId,courseId,enrollmentDate) values (?,?,?)",
                            (self.student_id, self.course_id,self. enrollment_date))

            print("Enrollment has been created")
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except InvalidCourseDataException as e:
            print(e)


    def get_payments_for_student(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student_id: "))
            cursor.execute("SELECT * FROM Payment WHERE studentId = ?",[(self.student_id)])
            records = cursor.fetchall()
            if records:
                print('_______Records In payment Table___')
            for i in records:
                print(i)
            else:
                conn.close()
        except PaymentValidationException as e:
            print(e)


    def get_payment_amount(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.student_id=int(input("enter student_id :"))
            cursor.execute("SELECT amount FROM Payment WHERE studentId = ?",[(self.student_id)])
            records = cursor.fetchall()
            if records:
                print('_______Records In payment Table___')
            for i in records:
                print(i)
            else:
                conn.close()
        except PaymentValidationException as e:
            print(e)


    def get_payment_date(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.student_id=int(input("enter student_id :"))

            cursor.execute("SELECT paymentDate  FROM Payment WHERE studentId = ?",[(self.student_id)])
            records = cursor.fetchall()
            if records:
                print('_______Records In payment Table___')
            for i in records:
                print(i)
            else:
                conn.close()
        except PaymentValidationException as e:
            print(e)

    def get_teacher_by_id(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.teacher_id = int(input("Enter teacher_id: "))
            cursor.execute("SELECT * FROM Teacher WHERE teacherId = ?",[(self.teacher_id )])
            records = cursor.fetchall()
            if records:
                print('_______Records In teacher Table___')
            for i in records:
                print(i)
            else:
                conn.close()
                raise InvalidTeacherDataException("entered teacher_id is not found")
        except TeacherNotFoundException as e:
            print(e)


    def update_student(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student id: "))
            self.first_name = input("Enter student first name: ")
            self.last_name = input("Enter student last name: ")
            self.date_of_birth = input("Enter student date of birth: ")
            self.email = input("Enter student email id: ")
            self.phone_number = input("Enter student phone number: ")
            cursor.execute(
                "UPDATE Student SET firstName = ?, lastName = ?, dateOfBirth = ?, email = ?, phoneNumber = ? WHERE studentId = ?",
                (self.first_name, self.last_name, self.date_of_birth, self.email, self.phone_number,self.student_id))
            print("Student has been updated")

            conn.commit()
            conn.close()
            return True
        except InvalidStudentDataException as e:
            print(e)

    def update_enrollment(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.enrollment_id = int(input("enrollment_id: "))
            self.student_id = int(input("Enter student_id: "))
            self.course_id = int(input("Enter course_id "))
            self.enrollment_date = input("Enter enrollment_date: ")

            cursor.execute(
                "UPDATE Enrollment SET  studentId=?, courseId=? , enrollmentDate=? WHERE enrollmentId = ?",
                (self.student_id,self.course_id,self.enrollment_date,self.enrollment_id))
            print("Enrollment has been updated")
            conn.commit()
            conn.close()
        except InvalidEnrollmentDataException as e:
            print(e)

    def update_payment(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.payment_id = int(input("Enter payment_id : "))
            self.student_id = int(input("Enter student_id: "))
            self.amount = int(input("Enter amount "))
            self.payment_date = input("Enter payment_date: ")

            cursor.execute(
            "UPDATE Payment SET   studentId=?, amount=?, paymentDate=? WHERE paymentId = ?",
            (self.payment_id,self.student_id,self.amount,self.payment_date))
            print("Payment has been updated")
            conn.commit()
            conn.close()
        except InsufficientFundsException as e:
            print(e)


    def update_course(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id: "))
            self.course_name = input("Enter course_name: ")
            self.course_code = input("Enter course_code ")
            self.teacher_id = int(input("Enter teacher_id: "))

            cursor.execute(
                "UPDATE Course SET courseName = ?, courseCode = ?, teacherId=? WHERE courseId = ?",
                (self.course_name, self.course_code,self.teacher_id,self.course_id))
            print("Course has been updated")
            conn.commit()
            conn.close()
        except InvalidCourseDataException as e:
            print(e)

    def update_teacher(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.teacher_id = int(input("Enter teacher id to update:"))
            self.first_name = input("Enter first name:")
            self.last_name = input("Enter last name:")
            self.email = input("Enter email:")
            sql = "UPDATE Teacher SET firstName = ?, lastName = ?, email = ? WHERE teacherId = ? "
            values = [(self.first_name, self.last_name, self.email, self.teacher_id)]
            print("Teacher has been updated")
            cursor.executemany(sql, values)
            conn.commit()
            conn.close()
        except InvalidTeacherDataException as e:
            print(e)

    def delete_student(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student_id to delete"))
            sql = "delete from  Student  WHERE studentId = ?"
            values = [(self.student_id)]

            cursor.execute(sql, values)
            print("Student has been deleted")
            conn.commit()
            conn.close()
        except StudentNotFoundException as e:
            print(e)

    def delete_enrollment(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.enrollment_id = int(input("Enter enrollment_id to delete"))
            sql = "delete from  Enrollment  WHERE enrollmentId = ?"
            values = [(self.enrollment_id)]

            cursor.execute(sql, values)
            print("Enrollment has been deleted")
            conn.commit()
            conn.close()
        except InvalidEnrollmentDataException as e:
            print(e)

    def delete_payment(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.payment_id = int(input("Enter payment_id to delete"))
            sql = "delete from  Payment  WHERE paymentId = ?"
            values = [self.payment_id]

            cursor.execute(sql, values)
            print("Payment has been deleted")
            conn.commit()
            conn.close()
        except PaymentValidationException as e:
            print(e)

    def delete_teacher(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.teacher_id = int(input("Enter teacher_id to delete"))
            sql = "delete from  Teacher  WHERE teacherId = ?"
            values = [self.teacher_id]

            cursor.execute(sql, values)
            print("Teacher has been deleted")
            conn.commit()
            conn.close()
        except TeacherNotFoundException as e:
            print(e)

    def delete_course(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id to delete"))
            sql = "delete from  Course  WHERE courseId = %s "
            values = [self.course_id]

            cursor.execute(sql, values)
            print("Course has been deleted")
            conn.commit()
            conn.close()
        except CourseNotFoundException as e:
            print(e)

    def make_payment(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student_id: "))
            self.amount = int(input("Enter amount "))
            self.payment_date = input("Enter payment_date: ")

            cursor.execute("INSERT INTO Payment (studentId, amount, paymentDate) VALUES (?,?,?,?)",
                           (self.student_id, self.amount,self.payment_date))
            print("Payment has been made")
            conn.commit()
            conn.close()
        except InsufficientFundsException as e:
            print(e)

    def get_enrolled_courses(self):
            try:
                conn = DBConnection.getConnection()
                cursor = conn.cursor()
                self.student_id = int(input("Enter student_id: "))
                cursor.execute("SELECT * FROM Students WHERE studentId = %s", [(self.student_id)])
                records = cursor.fetchall()
                if records:
                    print('_______Records In course Table___')
                for i in records:
                    print(i)
                else:
                    conn.close()
            except StudentNotFoundException as e:
                print(e)
    def assign_teacher(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id: "))
            self.teacher_id = int(input("Enter teacher id: "))

            cursor.execute(
                "update  Course set teacherId =? WHERE course_id = ? ",(self.teacher_id,self.course_id))
            print("Teacher has been updated")
            conn.commit()
            conn.close()
        except CourseNotFoundException as e:
            print(e)
    def get_courses_assigned_teacher(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.teacher_id= input("Enter teacher_id: ")

            cursor.execute(
                "select courseId,courseName from Course where teacherId=?", [(self.teacher_id)])
            conn.commit()
            conn.close()
        except  TeacherNotFoundException as e:
            print(e)

    def get_assigned_teacher_for_course(self):
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id: "))

            cursor.execute(
                "select teacherId from Course where courseId= ?",[(self.courseId)])
            conn.commit()
            conn.close()
        except TeacherNotFoundException as e:
            print(e)


