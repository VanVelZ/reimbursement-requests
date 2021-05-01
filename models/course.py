class Course:

    def __init__(self, name, start_date, end_date, cost, grading_format=None, id=None, type=None):
        self.name = name
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.grading_format = grading_format
        self.cost = cost
        self.id = id
