class GradingFormat:
    def __init__(self, type, requires_presentation=True, id=None):
        self.type = type
        self.requires_presentation = requires_presentation
        self.id = id

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "requiresPresentation": self.requires_presentation
        }

    @staticmethod
    def deserialize(json):
        return GradingFormat(type=json["type"], requires_presentation=json["requiresPresentation"], id=json["id"])