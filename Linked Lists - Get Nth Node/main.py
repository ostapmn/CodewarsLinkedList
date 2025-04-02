"""Linked Lists - Get Nth Node"""


class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node, index):
    current = node
    i = 0
    while i!=index:
        current = current.next
        i+=1
    return Node(current.data)
