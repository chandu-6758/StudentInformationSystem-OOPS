class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Student is already enrolled in the course"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class CourseNotFoundException(Exception):
    def __init__(self, message=" Course is not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class StudentNotFoundException(Exception):
    def __init__(self, message="Student  not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class TeacherNotFoundException(Exception):
    def __init__(self, message="Teacher not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class PaymentValidationException(Exception):
    def __init__(self, message="Error in payment validation"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid student data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid course data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid enrollment data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid teacher data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for operation"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message