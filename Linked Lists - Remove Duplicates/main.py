"""Linked Lists - Remove Duplicates"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Time out error
def remove_duplicates(head):
    lst = []
    if head is None:
        return None
    current = head
    prev = None
    while current:
        if current.data in lst:
            if prev:
                prev.next = current.next

            else:
                head = current.next
        else:
            lst.append(current.data)
            prev = current

        current = current.next
    return head
