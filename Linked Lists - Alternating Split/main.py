"""Linked Lists - Alternating Split"""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data} -> {self.next}"
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f"{self.first, self.second}"

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    i = 0
    current = head
    first = None
    second = None
    while current:
        if i%2 == 0:
            if first is None:
                first = Node(current.data)
                first_cur = first
            else:
                first_cur.next = Node(current.data)
                first_cur = first_cur.next
        else:
            if second is None:
                second = Node(current.data)
                second_cur = second
            else:
                second_cur.next = Node(current.data)
                second_cur = second_cur.next
        i += 1
        current = current.next
    return Context(first, second)

x = Node(1)
x.next = Node(2)
x.next.next = Node(3)
# x.next = Node(4)
# x.next = Node(5)
# x.next = Node(6)

print(alternating_split(x))


