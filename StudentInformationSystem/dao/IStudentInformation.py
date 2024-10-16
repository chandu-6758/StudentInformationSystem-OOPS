
from abc import ABC,abstractmethod
class SIS(ABC):

    @abstractmethod
    def create_student(self):
        pass

    @abstractmethod
    def create_course(self):
        pass

    @abstractmethod
    def create_enrollment(self):
        pass

    @abstractmethod
    def create_teacher(self):
        pass

    @abstractmethod
    def create_payment(self):
        pass

    @abstractmethod
    def get_student_by_id(self):
        pass

    @abstractmethod
    def get_course_by_id(self):
        pass

    @abstractmethod
    def get_enrollments_for_student(self):
        pass

    @abstractmethod
    def get_enrollments_for_course(self):
        pass

    @abstractmethod
    def enroll_in_course(self):
        pass

    @abstractmethod
    def get_payments_for_student(self):
        pass

    @abstractmethod
    def get_payment_amount(self):
        pass

    @abstractmethod
    def get_payment_date(self):
        pass

    @abstractmethod
    def get_teacher_by_id(self):
        pass

    @abstractmethod
    def update_student(self):
        pass

    @abstractmethod
    def update_enrollment(self):
        pass

    @abstractmethod
    def update_payment(self):
        pass

    @abstractmethod
    def update_course(self):
        pass

    @abstractmethod
    def update_teacher(self):
        pass

    @abstractmethod
    def delete_student(self):
        pass

    @abstractmethod
    def delete_enrollment(self):
        pass

    @abstractmethod
    def delete_payment(self):
        pass

    @abstractmethod
    def delete_teacher(self):
        pass

    @abstractmethod
    def delete_course(self):
        pass

    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def get_enrolled_courses(self):
        pass

    @abstractmethod
    def assign_teacher(self, teacher):
        pass

    @abstractmethod
    def get_assigned_courses(self):
        pass

    @abstractmethod
    def get_courses_assigned_teacher(self):
        pass

    @abstractmethod
    def get_assigned_teacher_for_course(self):
        pass
