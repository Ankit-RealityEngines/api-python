from .return_class import AbstractApiClass


class StreamingAuthToken(AbstractApiClass):
    """
        A streaming authentication token that is used to authenticate requests to append data to streaming datasets
    """

    def __init__(self, client, streamingToken=None, createdAt=None):
        super().__init__(client, None)
        self.streaming_token = streamingToken
        self.created_at = createdAt

    def __repr__(self):
        return f"StreamingAuthToken(streaming_token={repr(self.streaming_token)}, created_at={repr(self.created_at)})"

    def to_dict(self):
        return {'streaming_token': self.streaming_token, 'created_at': self.created_at}
