"""Can you get the loop ?"""

def loop_size(node):
    slow = node
    fast = node
    start = None

    while True:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = node
            while slow!=fast:
                slow = slow.next
                fast = fast.next
            start = slow
            slow = slow.next
            i = 1
            while slow!=start:
                i+=1
                slow = slow.next
            return i
