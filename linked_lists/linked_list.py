import unittest

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.val)
            current_node = current_node.next
        return "->".join(values)
    
    def __len__(self):
        counter = 0
        current_node = self.head
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter
    
    def to_list(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return values

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def iteractive_reverse(self):
        head = self.head
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next

            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        self.tail = head
        self.tail.next = None

    def recursive_reverse(self):
        pass

    def find_by_value(self, val):
        current_node = self.head
        while current_node.value != val and current_node.next:
            current_node = current_node.next
        if current_node.value == val:
            return current_node
        else:
            return None
    
    def find_previous_node(self, val):
        current_node = self.head
        if current_node.value == val:
            return None
        while current_node.next and current_node.next.value != val:
            current_node = current_node.next
        return current_node
    
    def append(self, list_node: ListNode):
        if not self.head:
            self.head = list_node
            self.tail = list_node
            return
        self.tail.next = list_node
        self.tail = self.tail.next

    def insert(self, val, list_node: ListNode):
        position = self.find_by_value(val)
        if position:
            list_node.next = position.next
            position.next = list_node
    
    def delete(self, val):
        if self.head and self.head.value == val:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        position = self.find_previous_node(val)
        if position and position.next:
            position.next = position.next.next
            if not position.next:
                self.tail = position
