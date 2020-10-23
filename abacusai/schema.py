

class Schema():
    '''

    '''

    def __init__(self, client, name=None, columnMapping=None, columnDataType=None):
        self.client = client
        self.id = None
        self.name = name
        self.column_mapping = columnMapping
        self.column_data_type = columnDataType

    def __repr__(self):
        return f"Schema(name={repr(self.name)}, column_mapping={repr(self.column_mapping)}, column_data_type={repr(self.column_data_type)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'name': self.name, 'column_mapping': self.column_mapping, 'column_data_type': self.column_data_type}
