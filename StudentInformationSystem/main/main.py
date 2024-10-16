
from dao.StudentInformationImpl import StudentInformationImpl

class MainModule:
    def __init__(self):
        self.service=StudentInformationImpl()

    def student_menu(self):
        while True:
            print("1.Create Student")
            print("2.Update Student")
            print("3.Delete Student")
            print("4.Display Student information")
            print("5.Student enrolled courses")
            print("6.Payments associated with Student")
            print("7.Return to Main Menu")

            option=input("Enter your choice: ")
            if option=="1":
                self.service.create_student()
            elif option=="2":
                self.service.update_student()
            elif option=="3":
                self.service.delete_student()
            elif option=="4":
                self.service.get_student_by_id()
            elif option=="5":
                self.service.get_enrolled_courses()
            elif option=="6":
                self.service.get_payments_for_student()
            elif option=="7":
                break
            else:
                print("Invalid option")

    def teacher_menu(self):
        while True:
            print("1.Create Teacher")
            print("2.Update Teacher")
            print("3.Delete Teacher")
            print("4.Display Teacher information")
            print("5.Teacher enrolled courses")
            print("6.Assign Teacher")
            print("7.Return to Main Menu")
            option=input("Enter your choice: ")
            if option=="1":
                self.service.create_teacher()
            elif option=="2":
                self.service.update_teacher()
            elif option=="3":
                self.service.delete_teacher()
            elif option=="4":
                self.service.get_teacher_by_id()
            elif option=="5":
                self.service.get_assigned_teacher_for_course()
            elif option=="6":
                self.service.assign_teacher()
            elif option=="7":
                break
            else:
                print("Invalid option")

    def course_menu(self):
        while True:
            print("1.Create Course")
            print("2.Update Course")
            print("3.Delete Course")
            print("4.Get Course by ID")
            print("5.Get assigned courses for the teacher")
            print("6.Return to Main Menu")
            option=input("Enter your choice: ")
            if option=="1":
                self.service.create_course()
            elif option=="2":
                self.service.update_course()
            elif option=="3":
                self.service.delete_course()
            elif option=="4":
                self.service.get_course_by_id()
            elif option=="5":
                self.service.get_courses_assigned_teacher()
            elif option=="6":
                break
            else:
                print("Invalid option")

    def enrollment_menu(self):
        while True:
            print("1.Create Enrollment")
            print("2.Update Enrollment")
            print("3.Delete Enrollment")
            print("4.Get Enrollments for Students")
            print("5.Get Enrollments for courses")
            print("6.Enroll in Course")
            print("7.Report")
            print("8.Return to Main Menu")
            option=input("Enter your choice: ")
            if option=="1":
                self.service.create_enrollment()
            elif option=="2":
                self.service.update_enrollment()
            elif option=="3":
                self.service.delete_enrollment()
            elif option=="4":
                self.service.get_enrollments_for_student()
            elif option=="5":
                self.service.get_enrollments_for_course()
            elif option=="6":
                self.service.enroll_in_course()
            elif option=="7":
                self.service.generate_report()
            elif option=="8":
                break
            else:
                print("Invalid option")

    def payment_menu(self):
        while True:
            print("1.Create Payment")
            print("2.Update Payment")
            print("3.Delete Payment")
            print("4.Make Payment")
            print("5.Get Payments for Students")
            print("6.Get Payment amount")
            print("7.Get payment Date")
            print("8.Return to Main Menu")
            option=input("Enter your choice: ")
            if option=="1":
                self.service.create_payment()
            elif option=="2":
                self.service.update_payment()
            elif option=="3":
                self.service.delete_payment()
            elif option=="4":
                self.service.make_payment()
            elif option=="5":
                self.service.get_payments_for_student()
            elif option=="6":
                self.service.get_payment_amount()
            elif option=="7":
                self.service.get_payment_date()
            elif option=="8":
                break
            else:
                print("Invalid option")



    def menu(self):
        menu=MainModule()
        while True:
            print("======Welcome to Student Information System======")
            print("Main Menu:")
            print("1.Students")
            print("2.Teachers")
            print("3.Courses")
            print("4.Enrollments")
            print("5.Payments")
            print("6.Exit")

            option=int(input("Enter your choice: "))
            if option==1:
                menu.student_menu()
            elif option==2:
                menu.teacher_menu()
            elif option==3:
                menu.course_menu()
            elif option==4:
                menu.enrollment_menu()
            elif option==5:
                menu.payment_menu()
            elif option==6:
                print("Thank you for using Student Information System")
                break
            else:
                print("Invalid option")


obj=MainModule()
obj.menu()

