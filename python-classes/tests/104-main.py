#!/usr/bin/python3
DoubleLinkedList = __import__('104-double_linked_list').LinkedList

sll = DoubleLinkedList()
sll.insert_at_begin(2)
sll.insert_at_begin(5)
sll.insert_at_begin(3)
sll.insert_at_begin(10)
sll.insert_at_begin(1)
sll.insert_at_final(-4)
sll.insert_at_final(-3)
sll.insert_at_final(4)
sll.insert_at_final(5)
sll.insert_at_final(12)
sll.insert_at_final(3)
sll.print()
print("----------------------------------------------------------------")
sll.print_rev()