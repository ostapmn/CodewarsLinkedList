"""Parse a linked list from a string"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def printf(self):
        current = self
        output = ''
        while current!=None:
            output+=str(current.data) + ' -> '
            current = current.next
        print(output.strip(' -> '))


def linked_list_from_string(s:str):
    s = s.split(' -> ')
    if s[0] == "None":
        head = None
        return None
    head = Node(int(s[0]) if s[0].isdigit() else s[0])
    current = head
    for _, el in enumerate(s[1:]):
        if el == "None":
            current.next = None
        else:
            current.next = Node(int(el))
            current = current.next

    return head
