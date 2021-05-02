class ReimbursementStatus:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def deserialize(json):
        return ReimbursementStatus(json["name"], json["id"])