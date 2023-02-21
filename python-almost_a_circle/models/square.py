#!/usr/bin/python3
"later"
from models.rectangle import Rectangle


class Square(Rectangle):
    "later"
    def __init__(self, size: int, x=0, y=0, id=None):
        "later"
        super().__init__(size, size, x, y, id)

    @property
    def size(self) -> int:
        "later"
        return self.height

    @size.setter
    def size(self, value: int) -> None:
        "later"
        self.width = value
        self.height = value

    def __str__(self) -> str:
        "later"
        return_value = f"[{self.__class__.__name__}] ({self.id})"
        return f"{return_value} {self.x}/{self.y} - {self.width}"
    
    def update(self, *args, **kwargs) -> None:
        "later"
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    self.__setattr__(key, value)

    def to_dictionary(self):
        "later"
        dictionary_representation = { "x": self.x, "y": self.y, "id": self.id, "size": self.size}
        return dictionary_representation
