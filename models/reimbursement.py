from models.course import Course
from models.employee import Employee
from models.reimbursement_status import ReimbursementStatus


class Reimbursement:

    def __init__(self, date_submitted, course=None, employee=None, status=None, amount=0, id=None, message=""):
        self.employee = employee
        self.status = status
        self.date_submitted = date_submitted
        self.course = course
        self.amount = amount
        self.id = id
        self.message = message

    def serialize(self):
        return {
            "id": self.id,
            "employee": self.employee.serialize(),
            "status": self.status.serialize(),
            "dateSubmitted": self.date_submitted,
            "course": self.course.serialize(),
            "amount": str(self.amount),
            "message": self.message
        }

    @staticmethod
    def deserialize(json):
        print(json)
        return Reimbursement(employee=Employee.deserialize(json["employee"]),
                             status=ReimbursementStatus.deserialize(json["status"]),
                             date_submitted=json["dateSubmitted"],
                             course=Course.deserialize(json["course"]),
                             amount=json["amount"],
                             message=json["message"],
                             id=json["id"])