class GradingFormat:
    def __init__(self, type, requires_presentation=True, id=None):
        self.type = type
        self.requires_presentation = requires_presentation
        self.id = id

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "requires_presentation": self.requires_presentation
        }

    @staticmethod
    def deserialize(json):
        return GradingFormat(json["type"], json["requires_presentation"], json["id"])