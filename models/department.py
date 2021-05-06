
class Department:
    def __init__(self, name, head=None, id=None):
        self.name = name
        self.head = head
        self.id = id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "head": self.head
        }

    @staticmethod
    def deserialize(json):
        return Department(json["name"], json["id"])