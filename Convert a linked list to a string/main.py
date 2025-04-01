"""Convert a linked list to a string"""


class Node:
    """Class for Node representing"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def stringify(node:Node) -> str:
    """Function to  turn Linked list into string"""
    current = node
    output = ''
    while current is not None:
        output += str(current.data) + ' -> '
        current = current.next
    return output + 'None'
