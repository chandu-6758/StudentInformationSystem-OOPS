class Enrollment:
    def __init__(self,enrollmentId,studentId,courseId,enrollmentDate):
        self.enrollmentId = enrollmentId
        self.studentId = studentId
        self.courseId = courseId
        self.enrollmentDate = enrollmentDate

    def set_enrollmentId(self,enrollmentId):
        self.enrollmentId = enrollmentId
    def set_studentId(self,studentId):
        self.studentId = studentId
    def set_courseId(self,courseId):
        self.courseId = courseId
    def set_enrollmentDate(self,enrollmentDate):
        self.enrollmentDate = enrollmentDate

    def get_enrollmentId(self):
        return self.enrollmentId
    def get_studentId(self):
        return self.studentId
    def get_courseId(self):
        return self.courseId
    def get_enrollmentDate(self):
        return self.enrollmentDate