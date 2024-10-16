class Teacher:
    def __init__(self,teacherId,firstName,lastName,email):
        self.teacherId = teacherId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def set_teacherId(self,teacherId):
        self.teacherId = teacherId
    def set_firstName(self,firstName):
        self.firstName = firstName
    def set_lastName(self,lastName):
        self.lastName = lastName
    def set_email(self,email):
        self.email = email

    def get_teacherId(self):
        return self.teacherId
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_email(self):
        return self.email