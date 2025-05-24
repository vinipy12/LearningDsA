"""
Given the head of a singly linked list, reverse the list, 
and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def reverseList(head: ListNode | None) -> ListNode | None:
    current_node = head
    prev_node = None
    while current_node:
        next_node = current_node.next

        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    head = prev_node
    return head