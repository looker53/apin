"""format convert"""
import yaml


class Case:
    """case data"""
    def __init__(self):
        self.data = None
        self.request_data = None

    @classmethod
    def from_yaml(cls, file, encoding='utf8'):
        """read data from yaml"""
        with open(file, encoding=encoding) as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            obj = cls()
            obj.data = data
            obj.request_data = data.get('request')
            return obj

    def from_json(self):
        """read data from json"""
        pass
