from .return_class import AbstractApiClass


class ModelLocation(AbstractApiClass):
    """

    """

    def __init__(self, client, location=None, artifactNames=None):
        super().__init__(client, None)
        self.location = location
        self.artifact_names = artifactNames

    def __repr__(self):
        return f"ModelLocation(location={repr(self.location)}, artifact_names={repr(self.artifact_names)})"

    def to_dict(self):
        return {'location': self.location, 'artifact_names': self.artifact_names}
