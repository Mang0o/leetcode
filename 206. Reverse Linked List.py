"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
         if head is None:
            return head

        current = head.next
        head.next = None
        while current:
            tmp = current.next
            current.next = head
            head = current
            current = tmp
        return head

    def reverseList_v2(self, head): #recursively
        """
        :type head: ListNode
        :rtype: ListNode
        """
        