class Reimbursement:

    def __init__(self, employee, status, date_submitted, course, amount=0, id=None):
        self.employee = employee
        self.status = status
        self.date_submitted = date_submitted
        self.course = course
        self.amount = amount
        self.id = id
