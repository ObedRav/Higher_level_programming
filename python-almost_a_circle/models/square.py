from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size: int, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self) -> int:
        return self.height

    @size.setter
    def size(self, value: int) -> None:
        self.width = value
        self.height = value

    def __str__(self) -> str:
        return_value = f"[{self.__class__.__name__}] ({self.id})"
        return f"{return_value} {self.x}/{self.y} - {self.width}"
    
    def update(self, *args, **kwargs) -> None:
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    self.__setattr__(key, value)

    def to_dictionary(self):
        dictionary_representation = { "x": self.x, "y": self.y, "id": self.id, "size": self.size}
        return dictionary_representation
