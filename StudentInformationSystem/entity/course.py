class Course:
    def __init__(self, courseId,courseName,courseCode, instructorName):
        self.courseId = courseId
        self.courseName = courseName
        self.courseCode = courseCode
        self.instructorName=instructorName

    def set_courseId(self,courseId):
        self.courseId = courseId
    def set_courseName(self,courseName):
        self.courseName = courseName
    def set_courseCode(self,courseCode):
        self.courseCode = courseCode
    def set_instructorName(self,instructorName):
        self.instructorName = instructorName

    def get_courseId(self):
        return self.courseId
    def get_courseName(self):
        return self.courseName
    def get_courseCode(self):
        return self.courseCode
    def get_instructorName(self):
        return self.instructorName
