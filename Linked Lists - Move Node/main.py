"""Linked Lists - Move Node"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError("Source linked list is empty")
    new_dest = Node(source.data)
    new_dest.next = dest
    source = source.next
    return Context(source, new_dest)
