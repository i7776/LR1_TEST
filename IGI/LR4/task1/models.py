import re

class JsonSerializeMixit:

    def to_dict(self):
        data = {}
        for key, value in vars(self).items():
            clean_key = re.sub(r'^_.*__', '', key)
            data [clean_key] = value

        return data

