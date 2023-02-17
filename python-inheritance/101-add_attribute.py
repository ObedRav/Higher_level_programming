
def add_attribute(object: object, name: str, value: str):
    if not isinstance(object, (int, float, str, bool)):
        object.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")