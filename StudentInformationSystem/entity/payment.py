class Payment:
    def __init__(self, paymentId,studentId,amount, paymentDate):
        self.paymentId = paymentId
        self.studentId = studentId
        self.amount = amount
        self.paymentDate = paymentDate

    def set_paymentId(self, paymentId):
        self.paymentId = paymentId
    def set_studentId(self, studentId):
        self.studentId = studentId
    def set_amount(self, amount):
        self.amount = amount
    def set_paymentDate(self, paymentDate):
        self.paymentDate = paymentDate

    def get_paymentId(self):
        return self.paymentId
    def get_studentId(self):
        return self.studentId
    def get_amount(self):
        return self.amount
    def get_paymentDate(self):
        return self.paymentDate
