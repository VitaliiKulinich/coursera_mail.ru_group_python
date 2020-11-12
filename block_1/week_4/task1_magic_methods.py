import os
import tempfile
import uuid


class File:
    def __init__(self, file, data=''):
        self.path_to_file = os.path.abspath(file)
        self.data = data
        self.current = 0
        if not os.path.exists(self.path_to_file):
            open(self.path_to_file, 'w').close()

    def __str__(self):
        return self.path_to_file

    def __add__(self, other_class):
        path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4().hex))
        new_object = File(path)
        new_object.write(self.read() + other_class.read())
        return new_object

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path_to_file, "r") as f:
            f.seek(self.current)
            line = f.readline()
            if not line:
                self.current = 0
                raise StopIteration
            self.current = f.tell()
            return line

    def read(self):
        with open(self.path_to_file, "r") as file:
            data = file.read()
        return data

    def write(self, text):
        with open(self.path_to_file, 'w') as file:
            file.write(text)
        return len(text)

