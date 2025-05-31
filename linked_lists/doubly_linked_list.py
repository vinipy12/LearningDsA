class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_front(self, val):
        list_node = ListNode(val)

        list_node.prev = None
        list_node.next = self.head
        self.head = list_node