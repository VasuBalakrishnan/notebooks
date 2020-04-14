import os
from pathlib import Path
import keyring

class Paths:

    @classmethod
    def data(self):
        current_path = Path(__file__)
        path = os.path.join(current_path.parent.parent, "data")
        if not os.path.exists(path):
            os.makedirs(path)

        return os.path.abspath(path)

class Secrets:

    @classmethod
    def get(cls, key):
        return keyring.get_password('system', key)