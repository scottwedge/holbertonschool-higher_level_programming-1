#!/usr/bin/python3
"""Class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format
               (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        list_a = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, list_a[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        keys = ['id', 'size', 'x', 'y']
        values = [self.id, self.width, self.x, self.y]
        return dict(zip(keys, values))
