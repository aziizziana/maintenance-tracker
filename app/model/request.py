class Request:
    def __init__(self, identifier, name, owner, status="unresolved"):
        self.identifier = identifier
        self.name = name
        self.owner = owner
        self.status = status

    def get_dict(self):
        return dict(identifier=self.identifier, name=self.name, owner=self.owner, status=self.status)
