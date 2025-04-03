"""Linked Lists - Remove Duplicates"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head:Node):
    if not head:
        return None
    lst = {head.data}
    current = head
    while current:
        if current.next and current.next.data in lst:
            current.next = current.next.next if current.next else None
        else:
            current = current.next
            lst.add(current.data if current else None)
    return head
