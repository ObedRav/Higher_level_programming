#!/usr/bin/python3

class Node():
    def __init__(self, data: int, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_at_begin(self, value: int):
        if not isinstance(value, (int, float)) and value is not None:
            raise ValueError("Value must be an integer")

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next_node = self.head
        self.head = new_node
        new_node.next_node.prev_node = new_node


    def insert_at_final(self, value: int):
        if not isinstance(value, (int, float)) and value is not None:
            raise ValueError("Value must be an integer")

        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return


        self.tail.next_node = new_node
        new_node.prev_node = self.tail
        self.tail = new_node
        

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_node

    def print_rev(self):
        current = self.tail
        
        while current:
            print(current.data)
            current = current.prev_node
