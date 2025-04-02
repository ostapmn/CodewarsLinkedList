"""Linked Lists - Push & BuildOneTwoThree"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def printf(self):
        current = self
        output = ''
        while current!=None:
            output+=str(current.data) + ' -> '
            current = current.next
        print(output.strip(' -> '))

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    head = Node(1)
    current = head
    for k in [2, 3]:
        current.next = Node(k)
        current = current.next
    return head