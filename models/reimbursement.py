from models.course import Course
from models.reimbursement_status import ReimbursementStatus


class Reimbursement:

    def __init__(self, date_submitted, course=None, employee_id=None, status=None, amount=0, id=None, message=""):
        self.employee_id = employee_id
        self.status = status
        self.date_submitted = date_submitted
        self.course = course
        self.amount = amount
        self.id = id
        self.message = message

    def serialize(self):
        return {
            "id": self.id,
            "employeeId": self.employee_id,
            "status": self.status.serialize(),
            "dateSubmitted": self.date_submitted,
            "course": self.course.serialize(),
            "amount": str(self.amount),
            "message": self.message
        }

    @staticmethod
    def deserialize(json):
        return Reimbursement(employee_id=json["employeeId"],
                             status=ReimbursementStatus.deserialize(json["status"]),
                             date_submitted=json["dateSubmitted"],
                             course=Course.deserialize(json["course"]),
                             amount=json["amount"],
                             message=json["message"],
                             id=json["id"])