class Student:
    def __init__(self, studentId,firstName, lastName, middleName, email, phoneNumber):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber

    def set_studentId(self, studentId):
        self.studentId = studentId

    def set_firstName(self, firstName):
        self.firstName = firstName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def set_email(self, email):
        self.email = email

    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def get_studentId(self):
        return self.studentId

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_email(self):
        return self.email

    def get_phoneNumber(self):
        return self.phoneNumber
