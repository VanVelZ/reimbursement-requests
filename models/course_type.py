class CourseType:
    def __init__(self, name, reimbursement_percent=0.3, id=None):
        self.name = name
        self.reimbursement_percent = reimbursement_percent
        self.id = id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "reimbursementPercent": str(self.reimbursement_percent)
        }

    @staticmethod
    def deserialize(json):
        return CourseType(json["name"], json["reimbursementPercent"], json["id"])