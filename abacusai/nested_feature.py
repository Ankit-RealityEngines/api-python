from .return_class import AbstractApiClass


class NestedFeature(AbstractApiClass):
    """
        A nested feature in a feature group
    """

    def __init__(self, client, name=None, selectClause=None, featureType=None, featureMapping=None, dataType=None, dataUse=None, sourceTable=None, originalName=None):
        super().__init__(client, None)
        self.name = name
        self.select_clause = selectClause
        self.feature_type = featureType
        self.feature_mapping = featureMapping
        self.data_type = dataType
        self.data_use = dataUse
        self.source_table = sourceTable
        self.original_name = originalName

    def __repr__(self):
        return f"NestedFeature(name={repr(self.name)}, select_clause={repr(self.select_clause)}, feature_type={repr(self.feature_type)}, feature_mapping={repr(self.feature_mapping)}, data_type={repr(self.data_type)}, data_use={repr(self.data_use)}, source_table={repr(self.source_table)}, original_name={repr(self.original_name)})"

    def to_dict(self):
        return {'name': self.name, 'select_clause': self.select_clause, 'feature_type': self.feature_type, 'feature_mapping': self.feature_mapping, 'data_type': self.data_type, 'data_use': self.data_use, 'source_table': self.source_table, 'original_name': self.original_name}
