"""Linked Lists - Sorted Insert"""


# For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head:Node, data:int):
    """Function to insert onject in correct position"""
    current = head
    while True:
        if current is None:
            head = Node(data)
            break
        if current.data > data:
            head = Node(data)
            head.next = current
            break
        if current.next is None or data <= current.next.data:
            x = Node(data)
            current.next, x.next = x, current.next
            break
        current = current.next
    return head