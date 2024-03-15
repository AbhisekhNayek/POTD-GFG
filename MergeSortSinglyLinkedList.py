class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def split(self, head):
        slow = head
        fast = head.next

        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next

        front = head
        back = slow.next
        slow.next = None

        return front, back

    def merge(self, a, b):
        dummy = Node(-1)
        tail = dummy
        dummy.next = None

        while a is not None and b is not None:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a is not None else b

        return dummy.next

    def sort(self, headRef):
        head = headRef[0]

        if head is None or head.next is None:
            return

        a, b = self.split(head)

        self.sort([a])
        self.sort([b])

        headRef[0] = self.merge(a, b)
