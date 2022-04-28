import json
import pickle
from pathlib import Path


class SimpleStore:
    def __init__(self, path):
        self.path = path
        self.data = {}

        if Path(self.path).is_file():
            self._read_db()

    def __str__(self):
        return json.dumps(self.data)

    def _read_db(self):
        with open(self.path, 'rb') as file:
            self.data = pickle.load(file)

    def set(self, key, value):
        self.data[key] = value

    def remove(self, key):
        del self.data[key]

    def dump(self):
        with open(self.path, 'wb') as file:
            pickle.dump(self.data, file)

    def get(self, key):
        return self.data[key]

    def data(self):
        return self.data

