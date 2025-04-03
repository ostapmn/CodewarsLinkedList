"""Swap Node Pairs In Linked List"""


class Node:
    def __init__(self, data, next=None):
        self.next = next

def swap_pairs(head:Node):
    if not head or not head.next:
        return head
    else:
        prev = head
        current = head.next
        prev.next = swap_pairs(current.next)
        current.next = prev
        return current
