from models.course_type import CourseType
from models.grading_format import GradingFormat


class Course:

    def __init__(self, name, start_date, end_date, cost, grading_format=None, id=None, type=None):
        self.name = name
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.grading_format = grading_format
        self.cost = cost
        self.id = id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type.serialize(),
            "startDate": self.start_date,
            "endDate": self.end_date,
            "gradingFormat": self.grading_format.serialize(),
            "cost": str(self.cost)
        }

    @staticmethod
    def deserialize(json):
        return Course(id=json["id"],
                      name=json["name"],
                      start_date=json["startDate"],
                      end_date=json["endDate"],
                      cost=json["cost"],
                      grading_format=GradingFormat.deserialize(json["gradingFormat"]),
                      type=CourseType.deserialize(json["type"]))
