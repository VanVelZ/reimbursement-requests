
class Role:
    def __init__(self, name="Unassigned", id=None):
        self.name = name
        self.id = id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def deserialize(json):
        return Role(json["name"], json["id"])