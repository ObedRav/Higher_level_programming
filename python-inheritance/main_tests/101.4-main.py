#!/usr/bin/python3

class MyClass():
     __slots__ = ["first_name"]

class MyClassInt(int):
    pass

a = MyClass()
b = MyClassInt()

print(type(a).__slots__)
print(type(b).__dict__)