"""Linked Lists - Recursive Reverse"""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def printf(self):
        current = self
        output = ''
        while current!=None:
            output+=str(current.data) + ' -> '
            current = current.next
        print(output.strip(' -> '))

def reverse(head):
    if head is None:
        return None
    def search(start:Node, arr:list = []):
        if start is None:
            return arr
        arr.insert(0, start.data)
        return search(start.next, arr)
    lst = search(head)
    head = Node(lst[0])
    current = head
    for el in lst[1:]:
        if el == None:
            continue
        current.next = Node(el)
        current = current.next
    return head
