#!/usr/bin/python3
""" This module is about define a Singly Linke List """


class Node:
    """ This class represents the node in the Singly Linke List"""
    def __init__(self, data: int, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ This class represents a list of linked lists """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value: int):
        """ This method is used to add a new item to the list """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __repr__(self) -> str:
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return '\n'.join(elements)
